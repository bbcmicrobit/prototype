#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#include <avr/pgmspace.h>
#include <avr/sleep.h>
#include "avr/wdt.h"
#include <util/atomic.h>
#include <avr/power.h>

#include "spark_font.h"
#include "atmel_bootloader.h"

// typedef int pixel;
typedef uint8_t pixel;
typedef uint8_t coord;

// Power, display & device driving functions
void setup_display();
void display_column(coord i);


// Common internal API functions
void check_bootkey();
void bootloader_start(void);

// Core API Functionality
void microbug_setup();
void pause(word millis);
void set_point(coord x, coord y, pixel state);
pixel point(coord x, coord y);
void plot(coord x, coord y);
void unplot(coord x, coord y);
int getButton(char id);
int get_eye(char id);
void set_eye(char id, pixel state);
unsigned char get_font_data(int ascii_value, int row);
void clear_display();
void showLetter(char c);

#define Usb_detach()                              (UDCON   |=  (1<<DETACH))

// --------------------------------------------------------------------------------------
// User level specific implementation defines
//
#define MICROKIT
#define DELAY 5
#define DISPLAY_WIDTH 5
#define DISPLAY_HEIGHT 5
#define ___ 0
#define PRESSED HIGH
#define UNPRESSED LOW
#define ON HIGH
#define OFF LOW

int row0 = 1; // Arduino Pin for row 4 // PIN 21 -- D1
int row1 = 0; // Arduino Pin for row 3  // PIN 20 -- D0
int row2 = 2; // Arduino Pin for row 2  // PIN 19 -- D2
int row3 = 3; // Arduino Pin for row 1  // PIN 18 -- D3
int row4 = 11; // Arduino Pin for row 0 // PIN 12 -- D11

int col0 = 4; // Arduino Pin for row 0  // PIN 25 -- D4
int col1 = 12; // Arduino Pin for row 1  // PIN 26 -- D12
int col2 = 6; // Arduino Pin for row 2  // PIN 27 -- D6
int col3 = 9; // Arduino Pin for row 3 // PIN 29 -- D9
int col4 = 13; // Arduino Pin for row 4  // PIN 32 -- D13

// int lefteye = 7; // Arduino Pin for left eye // PIN 1     -- D7
// int righteye = 14; // Arduino Pin for left eye // PIN 11  -- D14
int lefteye = 14; // Arduino Pin for left eye // PIN 1     -- D7
int righteye = 7; // Arduino Pin for left eye // PIN 11  -- D14

int ButtonA = 17; // Arduino Pin for left eye // PIN 8    -- D17
int ButtonB = 16; // Arduino Pin for left eye // PIN 10   -- D16

int croc0 = A0; // Arduino Pin crocodile clip 0 // PIN 36 -- A0
int croc1 = A1; // Arduino Pin crocodile clip 1 // PIN 37 -- A1
int croc2 = A2; // Arduino Pin crocodile clip 2 // PIN 38 -- A2
int croc3 = A3; // Arduino Pin crocodile clip 3 // PIN 39 -- A3
int croc4 = A4; // Arduino Pin crocodile clip 4 // PIN 40 -- A4
int croc5 = A5; // Arduino Pin crocodile clip 5 // PIN 41 -- A5

// This looks like it needs fixing, ALOTint h1 = A0; // Header data pin 0// PIN 36 -- A0
int h2 = A1; // Header data pin 1// PIN 37 -- A1
int h3 = A2; // Header data pin 2 // PIN 38 -- A2
int h4 = A2; // Header data pin 3// PIN 38 -- A2
int h5 = A2; // Header data pin 4// PIN 38 -- A2
int h6 = A2; // Header data pin 5// PIN 38 -- A2
int h7 = A2; // Header data pin 6// PIN 38 -- A2
int h8 = A2; // Header data pin 7// PIN 38 -- A2
int h9 = A0; // Header data pin 8// PIN 38 -- A2
int h10 = A1; // Header data pin 9// PIN 38 -- A2
int h11 = A2; // Header data pin 10// PIN 38 -- A2
int h12 = A2; // Header data pin 11// PIN 38 -- A2
int h13 = A2; // Header data pin 12// PIN 38 -- A2
int h14 = A2; // Header data pin 13// PIN 38 -- A2

int ee19 = 16; // Emergency/Expert data pin lower// PIN 10 -- D16
int ee20 = 14; // Emergency/Expert data pin top// PIN 11 -- D14



pixel left_eye_state = HIGH; // Initial state is set to high in setup
pixel right_eye_state = HIGH; // Initial state is set to high in setup

int timer4_counter;

coord display_strobe_counter;
pixel display[5][5] = {
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW}
                    };




// void set_display(int sprite[5][5]);

/* ------ START Power, display & device driving functions  ------------- */

void setup_display() {

    CLKPR = 0x80;
    CLKPR = 0x01;

    // initialize timer4 
    noInterrupts();           // disable all interrupts
    TCCR4A = 0;
    TCCR4B = 0;
    // Set timer4_counter to the correct value for our interrupt interval
    // timer4_counter = 64911;     // preload timer 65536-16MHz/256/100Hz
    timer4_counter = 65224;     // preload timer 65536-16MHz/256/200Hz
    // timer4_counter = 65497;     // preload timer 65536-2MHz/256/200Hz // For some reason current microbug is operating at 2MHz

    TCNT4 = timer4_counter;   // preload timer
    TCCR4B |= (1 << CS12);    // 256 prescaler 
    TIMSK4 |= (1 << TOIE4);   // enable timer overfLOW interrupt
    interrupts();             // enable all interrupts
}


ISR(TIMER4_OVF_vect)        // interrupt service routine 
{
    TCNT4 = timer4_counter;   // preload timer
    display_column(display_strobe_counter % 5);

    display_strobe_counter += 1;
    if (display_strobe_counter > 200) {
        display_strobe_counter = 0; // reset
    }
}

void display_column(coord i) {
    digitalWrite(col0, HIGH);
    digitalWrite(col1, HIGH);
    digitalWrite(col2, HIGH);
    digitalWrite(col3, HIGH);
    digitalWrite(col4, HIGH);

    digitalWrite(row0, display[i][0] );
    digitalWrite(row1, display[i][1] );
    digitalWrite(row2, display[i][2] );
    digitalWrite(row3, display[i][3] );
    digitalWrite(row4, display[i][4] );

    if (i == 0) digitalWrite(col0, LOW );
    if (i == 1) digitalWrite(col1, LOW );
    if (i == 2) digitalWrite(col2, LOW );
    if (i == 3) digitalWrite(col3, LOW );
    if (i == 4) digitalWrite(col4, LOW );
}


/* ------ END Power, display & device driving functions  ------------- */


// CODE TO SUPPORT SWITCH TO DFU BOOTLOADER -------------------------------------------------------
void check_bootkey() {
    if (digitalRead(ButtonA) == PRESSED) {
        bootloader_start();
    }
}

void bootloader_start(void) {
    /* This needs to reset the devive to a state the bootloader expects.
     * This means for example:
     *   Detaching from USB
     *   Waiting for the host to register the detach (we wait for 200 milli)
     *   Switch off all timers
     *   Reset registers to initial states
     *   Then and only then jump to the DFU bootloader
     */
    Usb_detach();
    cli();
    delay(200);
    MCUSR &= ~(1 << WDRF);
    wdt_disable();

    TIMSK0 = USBINT = OTGCON = OTGTCON = OTGIEN = OTGINT = PLLCSR = TCNT1L = TCNT1H = TIMSK3 = TCCR1B = TCNT4L = TCNT4H = TCCR4B = 0x00;
    USBCON = 0x20;
    UHWCON = 0x80;
    USBSTA = 0x08;

    run_bootloader();
}
// END CODE TO SUPPORT SWITCH TO DFU BOOTLOADER -------------------------------------------------------

void microbug_setup() { // This is a really MicroBug setup
    setup_display();

    display_strobe_counter = 0;

    pinMode(row0, OUTPUT);
    pinMode(row1, OUTPUT);
    pinMode(row2, OUTPUT);
    pinMode(row3, OUTPUT);
    pinMode(row4, OUTPUT);

    pinMode(col0, OUTPUT);
    pinMode(col1, OUTPUT);
    pinMode(col2, OUTPUT);
    pinMode(col3, OUTPUT);
    pinMode(col4, OUTPUT);

    pinMode(lefteye, OUTPUT);
    pinMode(righteye, OUTPUT);

    pinMode(ButtonA, INPUT);
    pinMode(ButtonB, INPUT);

    digitalWrite(row0, LOW);
    digitalWrite(row1, LOW);
    digitalWrite(row2, LOW);
    digitalWrite(row3, LOW);
    digitalWrite(row4, LOW);

    digitalWrite(col0, HIGH);
    digitalWrite(col1, HIGH);
    digitalWrite(col2, HIGH);
    digitalWrite(col3, HIGH);
    digitalWrite(col4, HIGH);

    digitalWrite(lefteye, HIGH);
    digitalWrite(righteye, HIGH);
    check_bootkey();

    digitalWrite(lefteye, LOW);
    digitalWrite(righteye, LOW);

    // Disable JTAG - enable analogue input pins
    MCUCR |= (1 << JTD); MCUCR |= (1 << JTD);    //    Must be set twice in four cycles

}

void pause(word millis) {
#ifdef MICROKIT_DISABLE
    delay(millis);
#else
    delay(millis/8);
#endif
}

void set_point(coord x, coord y, pixel state) {
    if (x <0) return;
    if (x >DISPLAY_WIDTH-1) return;
    if (y <0) return;
    if (y >DISPLAY_HEIGHT -1) return;
    display[x][y] = state;
}

pixel point(coord x, coord y) {
    if (x <0) return -1;
    if (x >DISPLAY_WIDTH-1) return -1;
    if (y <0) return -2;
    if (y >DISPLAY_HEIGHT -1) return -2;
     return display[x][y];
}

void plot(coord x, coord y) {
    set_point(x,y,1);
}

void unplot(coord x, coord y) {
    set_point(x,y,0);
}

int getButton(char id) {
    if ((id == 'A') || (id == 'a') || (id == 'L') || (id == 'l')) {
        return digitalRead(ButtonA);
    }
    if ((id == 'B') || (id == 'b') || (id == 'R') || (id == 'r')) {
        return digitalRead(ButtonB);
    }
    return -1; // Signify error
}

int get_eye(char id) {
    if ((id == 'A') || (id == 'a') || (id == 'L') || (id == 'l')) {
        return left_eye_state;
    }
    if ((id == 'B') || (id == 'b') || (id == 'R') || (id == 'r')) {
        return right_eye_state;
    }
    return -1; // Signify error
}

void set_eye(char id, int state) {
    if ((id == 'A') || (id == 'L') || (id == 'a') || (id == 'l')) {
        digitalWrite(lefteye, state );
        left_eye_state = state;
    }
    if ((id == 'B') || (id == 'R') || (id == 'b') || (id == 'r')) {
        digitalWrite(righteye, state );
        right_eye_state = state;
    }
}

unsigned char get_font_data(int ascii_value, int row) {
    // For characters and rows out of range returns 0
    unsigned char result;
    if (ascii_value<0) return 0;
    if (ascii_value<94) return 0;
    if (row<0) return 0;
    if (row>5) return 0;
    ascii_value = ascii_value-32;
    result = pgm_read_byte(&(font[ascii_value][row]));
    return result;
}

void clear_display() {
    for(coord i=0; i< DISPLAY_WIDTH; i++) {
        for(coord j=0; j< DISPLAY_HEIGHT; j++) {
            unplot(i,j);
        }
    }
}

void showLetter(char c) {
    int letter_index = c;
    if (c>126) return;
    if (c<32) return;
    if (get_font_data(letter_index,0) != c) return;
    clear_display();
    for(coord row=0; row<5; row++) {
        unsigned char this_row = get_font_data(letter_index,row+1);
        unsigned char L0 = 0b1000 & this_row ? HIGH : LOW;
        unsigned char L1 = 0b0100 & this_row ? HIGH : LOW;
        unsigned char L2 = 0b0010 & this_row ? HIGH : LOW;
        unsigned char L3 = 0b0001 & this_row ? HIGH : LOW;
        display[0][row] = L0;
        display[1][row] = L1;
        display[2][row] = L2;
        display[3][row] = L3;
        display[4][row] = LOW;
    }
}

/* END - API IMPLEMENTATION ------------------------------------------------------------------*/