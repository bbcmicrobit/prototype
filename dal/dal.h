
#include <avr/pgmspace.h>
#include <avr/sleep.h>
#include "avr/wdt.h"
#include <util/atomic.h>
#include <avr/power.h>
#include <avr/interrupt.h>

#include "spark_font.h"
#include "atmel_bootloader.h"

#define PRESSED HIGH
#define UNPRESSED LOW
#define ON HIGH
#define OFF LOW

#define MICROKIT
// #define MICROBUG
// #define Megabug

#ifdef MEGABUG

int row0 = 11; // Arduino Pin for row 0
int row1 = 3; // Arduino Pin for row 1
int row2 = 2; // Arduino Pin for row 2
int row3 = 4; // Arduino Pin for row 3
int row4 = 12; // Arduino Pin for row 4

int col0 = 6; // Arduino Pin for row 0
int col1 = 8; // Arduino Pin for row 1
int col2 = 9; // Arduino Pin for row 2
int col3 = 10; // Arduino Pin for row 3
int col4 = 5; // Arduino Pin for row 4

int lefteye = 7; // Arduino Pin for left eye
int righteye = 17; // Arduino Pin for left eye

int ButtonA = 15; // Arduino Pin for left button
int ButtonB = 16; // Arduino Pin for right button

#endif

#ifdef MICROBUG

int row0 = 12; // Arduino Pin for row 0
int row1 = 4; // Arduino Pin for row 1
int row2 = 2; // Arduino Pin for row 2
int row3 = 3; // Arduino Pin for row 3
int row4 = 11; // Arduino Pin for row 4

int col0 = 6; // Arduino Pin for row 0
int col1 = 8; // Arduino Pin for row 1
int col2 = 9; // Arduino Pin for row 2
int col3 = 10; // Arduino Pin for row 3
int col4 = 5; // Arduino Pin for row 4

int lefteye = 7; // Arduino Pin for left eye
int righteye = 17; // Arduino Pin for left eye

int ButtonA = 16; // Arduino Pin for left button
int ButtonB = 15; // Arduino Pin for right button

#endif

#ifdef MICROKIT

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

int lefteye = 14; // Arduino Pin for left eye // PIN 1     -- D7
int righteye = 7; // Arduino Pin for left eye // PIN 11  -- D14

int ButtonA = 17; // Arduino Pin for left button // PIN 8    -- D17
int ButtonB = 16; // Arduino Pin for right button // PIN 10   -- D16

int croc0 = A0; // Arduino Pin crocodile clip 0 // PIN 36 -- A0
int croc1 = A1; // Arduino Pin crocodile clip 1 // PIN 37 -- A1
int croc2 = A2; // Arduino Pin crocodile clip 2 // PIN 38 -- A2
int croc3 = A3; // Arduino Pin crocodile clip 3 // PIN 39 -- A3
int croc4 = A4; // Arduino Pin crocodile clip 4 // PIN 40 -- A4
int croc5 = A5; // Arduino Pin crocodile clip 5 // PIN 41 -- A5


int h1 = A0; // Header data pin 0// PIN 36 -- A0
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

#endif

#define DELAY 5

int left_eye_state = HIGH; // Initial state is set to high in setup
int right_eye_state = HIGH; // Initial state is set to high in setup
int timer4_counter;


int display_strobe_counter;
int display[5][5] = {                                    // DONE
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW}
                    };

int sleep_time = 3; // This is the time in minutes before the device switches off
                     // Having it as a variable allows the user to override this.
long sleep_counter_t = 0;
long sleep_counter_t2 = 0;


/* API ---------------------------------------------------------------------------------------- */

// DONE
#define DISPLAY_WIDTH 5
#define DISPLAY_HEIGHT 5

// DONE
#define ___ 0

// DONE
typedef struct Image {
    int width;
    int height;
    int *data ;
//    unsigned char *data;
} Image;



int get_eye(char id);
void set_eye(char id, int state);// DONE
void eye_on(char id); // DONE
void eye_off(char id);// DONE

int get_eye(char *id);
void set_eye(const char *id, int state);// DONE
void eye_on(const char *id);// DONE
void eye_off(const char *id);// DONE

int getButton(char id);// DONE
int getButton(char *id); // Alternative for handling data from python code

// These next two functions should be deleted - they're there as crutches for the blockly front end.
// However, they need to be there for the moment (2015/01/05)

int get_button(char id);// DONE
int get_button(char *id); // Alternative for handling data from python code


void clear_display();// DONE
void plot(int x, int y);// DONE
void unplot(int x, int y);// DONE
int point(int x, int y);// DONE
void set_display(int sprite[5][5]);// DONE
void showViewport(Image& someImage, int x, int y);// DONE
void ScrollImage(Image someImage, boolean loop, int trailing_spaces);// DONE
int image_point(Image& someImage, int x, int y);// DONE
void set_image_point(Image& someImage, int x, int y, int value);// DONE
void showLetter(char c); // Could be just internal, but useful.
void showLetter(char * c);  // Alternative for handling data from python code

void show_letter(char c); // Could be just internal, but useful.
void show_letter(char * c);  // Alternative for handling data from python code


void print_message(const char * message, int pausetime);
void print_message(int number, int pausetime);

void toggle_eye(char id);// DONE
void toggle_eye(const char *id);

struct StringImage;// DONE
void scroll_string_image(StringImage theSprite, int pausetime);// DONE

// Functions internal to the API
inline int image_point_index(Image& someImage, int x, int y);// DONE
void display_column(int i);// DONE
void setup_display();// DONE
void microbug_setup();// DONE
void bootloader_start(void);
void check_bootkey();// DONE

// Crutch during development
void scroll_string(const char * str); // FIXME: Crutch during development// DONE
void scroll_string(const char * str, int delay); // FIXME: Crutch during development// DONE


/* END API ------------------------------------------------------------------------------------ */

/* START POWER OPTIMISATIONS ------------------------------------------------------------------------------------ */
// The power optimisations are courtesy of the "Sleepy" code from JeeLabs.
// Sleepy is (C) Jean-Claude Wippler 2014, used under the MIT License from - https://github.com/jcw/jeelib/blob/master/LICENSE



class Sleepy {
public:
    /// start the watchdog timer (or disable it if mode < 0)
    /// @param mode Enable watchdog trigger after "16 << mode" milliseconds 
    ///             (mode 0..9), or disable it (mode < 0).
    /// @note If you use this function, you MUST included a definition of a WDT
    /// interrupt handler in your code. The simplest is to include this line:
    ///
    ///     ISR(WDT_vect) { Sleepy::watchdogEvent(); }
    ///
    /// This will get called when the watchdog fires.
    static void watchdogInterrupts (char mode);

    /// enter low-power mode, wake up with watchdog, INT0/1, or pin-change
    static void powerDown ();

    /// Spend some time in low-power mode, the timing is only approximate.
    /// @param msecs Number of milliseconds to sleep, in range 0..65535.
    /// @returns 1 if all went normally, or 0 if some other interrupt occurred
    /// @note If you use this function, you MUST included a definition of a WDT
    /// interrupt handler in your code. The simplest is to include this line:
    ///
    ///     ISR(WDT_vect) { Sleepy::watchdogEvent(); }
    ///
    /// This will get called when the watchdog fires.
    static byte loseSomeTime (word msecs);

    /// This must be called from your watchdog interrupt code.
    static void watchdogEvent();
};

static volatile byte watchdogCounter;
void Sleepy::watchdogInterrupts (char mode) {
    // correct for the fact that WDP3 is *not* in bit position 3!
    if (mode & bit(3))
        mode ^= bit(3) | bit(WDP3);
    // pre-calculate the WDTCSR value, can't do it inside the timed sequence
    // we only generate interrupts, no reset
    byte wdtcsr = mode >= 0 ? bit(WDIE) | mode : 0;
    MCUSR &= ~(1<<WDRF);
    ATOMIC_BLOCK(ATOMIC_FORCEON) {
#ifndef WDTCSR
#define WDTCSR WDTCR
#endif
        WDTCSR |= (1<<WDCE) | (1<<WDE); // timed sequence
        WDTCSR = wdtcsr;
    }
}


// ISR(WDT_vect) { Sleepy::watchdogEvent(); }

/// @fn static void Sleepy::powerDown ();
/// Take the ATmega into the deepest possible power down state. Getting out of
/// this state requires setting up the watchdog beforehand, or making sure that
/// suitable interrupts will occur once powered down.
/// Disables the Brown Out Detector (BOD), the A/D converter (ADC), and other
/// peripheral functions such as TWI, SPI, and UART before sleeping, and
/// restores their previous state when back up.
void Sleepy::powerDown () {
    byte adcsraSave = ADCSRA;
    ADCSRA &= ~ bit(ADEN); // disable the ADC
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);
    ATOMIC_BLOCK(ATOMIC_FORCEON) {
        sleep_enable();
        // sleep_bod_disable(); // can't use this - not in my avr-libc version!
#ifdef BODSE
        MCUCR = MCUCR | bit(BODSE) | bit(BODS); // timed sequence
        MCUCR = (MCUCR & ~ bit(BODSE)) | bit(BODS);
#endif
    }
    sleep_cpu();
    sleep_disable();
    // re-enable what we disabled
    ADCSRA = adcsraSave;
}

byte Sleepy::loseSomeTime (word msecs) {
    byte ok = 1;
    word msleft = msecs;
    // only slow down for periods longer than the watchdog granularity
    while (msleft >= 16) {
        char wdp = 0; // wdp 0..9 corresponds to roughly 16..8192 ms
        // calc wdp as log2(msleft/16), i.e. loop & inc while next value is ok
        for (word m = msleft; m >= 32; m >>= 1)
            if (++wdp >= 9)
                break;
        watchdogCounter = 0;
        watchdogInterrupts(wdp);
        powerDown();
        watchdogInterrupts(-1); // off
        // when interrupted, our best guess is that half the time has passed
        word halfms = 8 << wdp;
        msleft -= halfms;
        if (watchdogCounter == 0) {
            ok = 0; // lost some time, but got interrupted
            break;
        }
        msleft -= halfms;
    }
    // adjust the milli ticks, since we will have missed several
#if defined(__AVR_ATtiny84__) || defined(__AVR_ATtiny85__) || defined (__AVR_ATtiny44__) || defined (__AVR_ATtiny45__)
    extern volatile unsigned long millis_timer_millis;
    millis_timer_millis += msecs - msleft;
#else
    extern volatile unsigned long timer0_millis;
    timer0_millis += msecs - msleft;
#endif
    return ok; // true if we lost approx the time planned
}

void Sleepy::watchdogEvent() {
    ++watchdogCounter;
}



void pause(word millis) {
#ifdef MICROKIT_DISABLE
    delay(millis);
#else
    delay(millis/8);
#endif
}

void sleep(word millis) {
    Sleepy::loseSomeTime( millis);
}


void enable_power_optimisations() {
    // Disable lots of things - we need to be able to re-enable these, but not at present

    power_adc_disable();
    power_usart0_disable();
    power_spi_disable();
    power_twi_disable();
    power_timer1_disable();
    power_timer2_disable();
    power_timer3_disable();
    power_usart1_disable();

    // Some registers need to be written to twice to cause them to be acted upon.
    (UDCON   |=  (1<<DETACH));           // Detach USB
    power_usb_disable();                 // Disable USB power
    USBCON |= (1 << FRZCLK);             // Stop USB Clock
    PLLCSR &= ~(1 << PLLE);              // Disable USB Clock
    USBCON &=  ~(1 << USBE  );           // Disable USB 
    UDINT  &= ~(1 << SUSPI);             // Really suspend USB
    USBCON |= ( 1 <<FRZCLK);             // Really freeze the USB clock
    PLLCSR &= ~(1 << PLLE);              // Really disable USB

    CLKSEL0 |= (1 << RCE);                  // Enable internal RC clock
    while ( (CLKSTA & (1 << RCON)) == 0){}  // Wait for the internal RC clock to be ready
    CLKSEL0 &= ~(1 << CLKS);                // Select the internal RC clock
    CLKSEL0 &= ~(1 << EXTE);                // Disable external clock

    clock_prescale_set(clock_div_8);        // Switch the CPU speed right down.
}

/* END POWER OPTIMISATIONS ------------------------------------------------------------------------------------ */



// CODE TO SUPPORT SWITCH TO DFU BOOTLOADER -------------------------------------------------------


#define Usb_detach()                              (UDCON   |=  (1<<DETACH))

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
    pause(200);
    MCUSR &= ~(1 << WDRF);
    wdt_disable();

    TIMSK0 = USBINT = OTGCON = OTGTCON = OTGIEN = OTGINT = PLLCSR = TCNT1L = TCNT1H = TIMSK3 = TCCR1B = TCNT4L = TCNT4H = TCCR4B = 0x00;
    USBCON = 0x20;
    UHWCON = 0x80;
    USBSTA = 0x08;

    run_bootloader();
}

void check_bootkey() {
    if (digitalRead(ButtonA) == PRESSED) {
        bootloader_start();
    }
}
// END CODE TO SUPPORT SWITCH TO DFU BOOTLOADER -------------------------------------------------------

void setup_display() {
#ifdef MICROBUG

CLKPR = 0x80;
CLKPR = 0x01;
#endif

#ifdef MICROKIT_DISABLE

CLKPR = 0x80;
CLKPR = 0x01;
#endif

    // initialize timer4 
    noInterrupts();           // disable all interrupts
    TCCR4A = 0;
    TCCR4B = 0;
    // Set timer4_counter to the correct value for our interrupt interval
    // timer4_counter = 64911;     // preload timer 65536-16MHz/256/100Hz
//    timer4_counter = 65224;     // preload timer 65536-16MHz/256/200Hz
//    timer4_counter = 65380;     // preload timer 65536-16MHz/256/400Hz
//    timer4_counter = 65458;     // preload timer 65536-16MHz/256/800Hz
    timer4_counter = 65224;     // 65536-(2000000/64/2000)

    // timer4_counter = 65497;     // preload timer 65536-2MHz/256/200Hz // For some reason current microbug is operating at 2MHz

    TCNT4 = timer4_counter;   // preload timer
    TCCR4B |= (0 << CS12);    //
    TCCR4B |= (0 << CS11);    // 64 prescaler 
    TCCR4B |= (1 << CS10);    // 64 prescaler 

    TIMSK4 |= (1 << TOIE4);   // enable timer overfLOW interrupt
    interrupts();             // enable all interrupts
}


ISR(TIMER4_OVF_vect)        // interrupt service routine 
{
    TCNT4 = timer4_counter;   // preload timer
        int col = display_strobe_counter % 20;

        if (col == 0) {
            digitalWrite(lefteye, left_eye_state);
            digitalWrite(righteye, right_eye_state);
        }
        if (col == 1) {
             digitalWrite(lefteye, LOW);
             digitalWrite(righteye, LOW);
        }
        if (col <5) {
            display_column(col % 5);
        }
        if (col == 5) {
            digitalWrite(row0, LOW);
            digitalWrite(row1, LOW);
            digitalWrite(row2, LOW);
            digitalWrite(row3, LOW);
            digitalWrite(row4, LOW);

            digitalWrite(col0, LOW);
            digitalWrite(col1, LOW);
            digitalWrite(col2, LOW);
            digitalWrite(col3, LOW);
            digitalWrite(col4, LOW);
            digitalWrite(lefteye, LOW);
            digitalWrite(righteye, LOW);
        }
//     }

//     if (display_strobe_counter == 0) {
//          digitalWrite(lefteye, left_eye_state);
//          digitalWrite(righteye, right_eye_state);
//     }
//     if (display_strobe_counter == 1) {
//          digitalWrite(lefteye, LOW);
//          digitalWrite(righteye, LOW);
//     }
//     if (display_strobe_counter <5) {
//         display_column(display_strobe_counter % 5);
//     }
//     if (display_strobe_counter == 5) {
//         digitalWrite(row0, LOW);
//         digitalWrite(row1, LOW);
//         digitalWrite(row2, LOW);
//         digitalWrite(row3, LOW);
//         digitalWrite(row4, LOW);
// 
//         digitalWrite(col0, LOW);
//         digitalWrite(col1, LOW);
//         digitalWrite(col2, LOW);
//         digitalWrite(col3, LOW);
//         digitalWrite(col4, LOW);
//         digitalWrite(lefteye, LOW);
//         digitalWrite(righteye, LOW);
// 
//     }
    display_strobe_counter += 1;
    if (display_strobe_counter >= 200) {
        display_strobe_counter = 0; // reset
    }
    if (sleep_time > 0) {
        sleep_counter_t = sleep_counter_t + 1;
        if (sleep_counter_t==28000) { // This is the number of times the display interrupt runs per 30 seconds, approximately.
           sleep_counter_t = 0;
           sleep_counter_t2 = sleep_counter_t2 + 1;
        }
        if (sleep_counter_t2 >= sleep_time*2) {
            // It's possible that the display will freeze with pins high, which isn't what we want.
            // As a result we force pins low.
            digitalWrite(row0, LOW);
            digitalWrite(row1, LOW);
            digitalWrite(row2, LOW);
            digitalWrite(row3, LOW);
            digitalWrite(row4, LOW);

            digitalWrite(col0, LOW);
            digitalWrite(col1, LOW);
            digitalWrite(col2, LOW);
            digitalWrite(col3, LOW);
            digitalWrite(col4, LOW);
            digitalWrite(lefteye, LOW);
            digitalWrite(righteye, LOW);

            set_sleep_mode(SLEEP_MODE_PWR_DOWN);
            cli();                // disable global interrupts
            sleep_enable();
            sleep_cpu();
        }
    }
}

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

    digitalWrite(lefteye, HIGH);  // Turn status LEDs on prior to checking bootkey
    digitalWrite(righteye, HIGH); // If we reboot they will stay on.

check_bootkey();  //. This will never return if we reboot device.

    digitalWrite(lefteye, LOW);
    digitalWrite(righteye, LOW);
}

void display_column(int i) {
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


void set_display(int sprite[5][5]) {
    for(int i=0; i<5; i++) {
        for(int j=0; j<5; j++) {
            display[i][j] = sprite[i][j];
        }
    }
}

void plot(int x, int y) {
    if (x <0) return;
    if (x >DISPLAY_WIDTH-1) return;

    if (y <0) return;
    if (y >DISPLAY_HEIGHT -1) return;

     display[x][y] = HIGH;
}

void unplot(int x, int y) {
    if (x <0) return;
    if (x >DISPLAY_WIDTH-1) return;

    if (y <0) return;
    if (y >DISPLAY_HEIGHT -1) return;

     display[x][y] = LOW;
}

int point(int x, int y) {
    // Bounds checking
    if (x <0) return -1;
    if (x >DISPLAY_WIDTH-1) return -1;

    if (y <0) return -2;
    if (y >DISPLAY_HEIGHT -1) return -2;

     return display[x][y];
}

inline int image_point_index(Image& someImage, int x, int y) {
   return x*someImage.width +y;
}

int image_point(Image& someImage, int x, int y) {
    if (x<0) return -1;
    if (y<0) return -2;
    if (x>someImage.width-1) return -1;
    if (x>someImage.height-1) return -2;

    return someImage.data[image_point_index(someImage, x, y)];
}

void set_image_point(Image& someImage, int x, int y, int value) {
    if (x<0);
    if (y<0);
    if (x>someImage.width-1);
    if (x>someImage.height-1);

    someImage.data[image_point_index(someImage, x, y)] = value;
}


void clear_display() {
    for(int i=0; i< DISPLAY_WIDTH; i++) {
        for(int j=0; j< DISPLAY_HEIGHT; j++) {
            unplot(i,j);
        }
    }
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

int get_eye(char *id) {
    return get_eye(*id);
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


int getButton(char *id){
    return getButton(*id);
}

// These next two functions should be deleted - they're there as crutches for the blockly front end.
// However, they need to be there for the moment (2015/01/05)

int get_button(char *id){
    return getButton(*id);
}

int get_button(char id){
    return getButton(id);
}

void showLetter(char * c) {
    showLetter(*c);
}

void show_letter(char * c) {
    showLetter(*c);
}

void show_letter(char c) {
    showLetter(c);
}

void showLetter(char c) {
    int letter_index = c-32;
    if (c>126) return;
    if (c<32) return;
    if (pgm_read_byte(&(font[letter_index][0])) != c) return;
    clear_display();
    for(int row=0; row<5; row++) {
        unsigned char this_row = pgm_read_byte(&(font[letter_index][row+1]));
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

void print_message(const char * message, int pausetime=100) {
    while(*message) {
        showLetter(*message);
        message++;
        pause(pausetime);
    }
}

void print_message(char * message, int pausetime=100) {
    while(*message) {
        showLetter(*message);
        message++;
        pause(pausetime);
    }
}

void print_message(int number, int pausetime) {
    char num_buf[14];
    itoa(number, num_buf, 10);
    print_message(num_buf, 10);
}


void set_eye(char id, int state) {
    if ((id == 'A') || (id == 'L')) {
//        digitalWrite(lefteye, state );
        left_eye_state = state;
    }
    if ((id == 'B') || (id == 'R')) {
//        digitalWrite(righteye, state );
        right_eye_state = state;
    }
}

void set_eye(const char * id, int state) {
    set_eye(*id, state);
}

void toggle_eye(char id) {
    if ((id == 'A') || (id == 'L')) {
        if (left_eye_state == HIGH) {
            set_eye(id, LOW);
        } else {
            set_eye(id, HIGH);
        }
    }
    if ((id == 'B') || (id == 'R')) {
        if (right_eye_state == HIGH) {
            set_eye(id, LOW);
        } else {
            set_eye(id, HIGH);
        }
    }
}

void toggle_eye(const char *id){
    toggle_eye(*id);
}

void eye_on(char id) {
    set_eye(id, HIGH);
}

void eye_on(const char *id) {
    set_eye(*id, HIGH);
}


void eye_off(char id) {
    set_eye(id, LOW);
}

void eye_off(const char *id) {
    set_eye(*id, LOW);
}

void showViewport(Image& someImage, int x, int y) {
    if (someImage.width<4) return; // Not implemented yet
    if (someImage.height<4) return; // Not implemented yet
    for(int i=0; (i+x<someImage.width) && (i<5); i++) {
        for(int j=y; (j+y<someImage.height) && (j<5); j++) {
            int value = someImage.data[(j+y)*someImage.width+ x+i ];
            display[i][j]=value;
        }
    }
}

void ScrollImage(Image someImage, boolean loop=false, int trailing_spaces=false) {
    // Example, width is 16
    // Display width is 5
    // This counts from 0 <= i < 12 -- ie from 0 to 11
    // The last viewport therefore tries to display indices 11, 12, 13, 14, 15
    for(int i=0; i<someImage.width-DISPLAY_WIDTH+1; i++) {
        clear_display();
        showViewport(someImage, i,0);
        pause(80);
    }
}

typedef struct StringImage {
    int mPixelPos;
    int mPixelData[50]; // Sufficient to hold two characters.
    char *mString;
    int mStrlen;
    char num_buf[12] ; 

    StringImage() {}
    StringImage(const char * str) {
        setString(str);
    }
    StringImage(int number) {
        itoa(number, num_buf, 10);
        setString(num_buf);
    }
    StringImage(long number) {
        itoa(number, num_buf, 10);
        setString(num_buf);
    }
    ~StringImage() {}

    void setString(const char * str) {
        mString = (char *) str;
        mPixelPos = 0;
        for(int i=0; i<50; i++) {
            mPixelData[i] = 0;
        }
        mStrlen = strlen(mString);
    }

    void update_display() {
        Image myImage;
        int mPP = mPixelPos%5;
        myImage.width=10;
        myImage.height=5;
        myImage.data = mPixelData;
        showViewport(myImage, mPP,0);

    }
    void render_string(){
        // Renders into the pixel data buffer
        int first_char =0;
        int second_char =0;
        unsigned char first_char_data1[6];
        unsigned char second_char_data1[16];
        int char_index1;
        int char_index0;

        int vPixelPos = mPixelPos -5;

        if (vPixelPos <0) {
            first_char = 0;
            second_char = mString[0]-32;
        } else {
            char_index0 = (vPixelPos / 5);
            char_index0 = char_index0 % mStrlen;
            char_index1 = (char_index0 +1) ;
            first_char = mString[char_index0] -32;
            if (char_index1 < mStrlen) {
                char_index1 = char_index1 % mStrlen;
                second_char = mString[char_index1]-32;
            }
        }

        for(int i=0; i<6; i++){
            first_char_data1[i] = pgm_read_byte(&(font[first_char][i]));
        }
        for(int i=0; i<6; i++){
            second_char_data1[i] = pgm_read_byte(&(font[second_char][i]));
        }

        for(int row=0; row<5; row++) {
            int row_first = first_char_data1[row + 1];
            int row_second = second_char_data1[row + 1];

            int F0 = 0b1000 & row_first ? HIGH : LOW;
            int F1 = 0b0100 & row_first ? HIGH : LOW;
            int F2 = 0b0010 & row_first ? HIGH : LOW;
            int F3 = 0b0001 & row_first ? HIGH : LOW;

            int S0 = 0b1000 & row_second ? HIGH : LOW;
            int S1 = 0b0100 & row_second ? HIGH : LOW;
            int S2 = 0b0010 & row_second ? HIGH : LOW;
            int S3 = 0b0001 & row_second ? HIGH : LOW;

            mPixelData[0+row*10] = F0;
            mPixelData[1+row*10] = F1;
            mPixelData[2+row*10] = F2;
            mPixelData[3+row*10] = F3;
            mPixelData[4+row*10] = 0;

            mPixelData[5+row*10] = S0;
            mPixelData[6+row*10] = S1;
            mPixelData[7+row*10] = S2;
            mPixelData[8+row*10] = S3;
            mPixelData[9+row*10] = 0;
        }
        update_display();
    }
    void pan_right() {
        // Move the viewport 1 pixel to the right. (Looks like scrolling left)
        mPixelPos += 1;
        if (mPixelPos>=pixel_width()) {
            mPixelPos =0;
        }
    }
    int pixel_width() {
        return mStrlen * 5;
    }
} StringImage;

void scroll_string_image(StringImage theSprite, int pausetime=100) {
    for(int i=0; i<theSprite.pixel_width(); i++) {
        theSprite.render_string();
        theSprite.pan_right();
        pause(pausetime);
    }
}

void scroll_string(const char * str) {
    scroll_string_image(StringImage(str), 50);
}
void scroll_string(const char * str, int delay) {
    scroll_string_image(StringImage(str), delay);
}

typedef int pxl;

Image& _make_image(unsigned short int row1, unsigned short int row2, unsigned short int row3, unsigned short int row4, unsigned short int row5, int width) 
{
    unsigned short int rows[5];
    rows[0] = row5;
    rows[1] = row4;
    rows[2] = row3;
    rows[3] = row2;
    rows[4] = row1;

    Image* img = (Image*) malloc(sizeof(Image));
    img->width = width;
    img->height = 5;
    img->data = (pxl *) malloc(img->width * img->height * sizeof(pxl));

    pxl *pData = img->data;

    for(int y=0; y < img->height; y++)
        for(int x=0; x < img->width; x++)
            *pData++ = (rows[y] & (1<<x)) ? HIGH : LOW;
    Image& retVal = *img;
    return retVal;
}

Image& make_image(unsigned short int row1, unsigned short int row2, unsigned short int row3, unsigned short int row4, unsigned short int row5)
{
    return _make_image(row1, row2, row3, row4, row5, 5);
}

Image& make_big_image(unsigned short int row1, unsigned short int row2, unsigned short int row3, unsigned short int row4, unsigned short int row5)
{
    return _make_image(row1, row2, row3, row4, row5, 10);
}

void OLD_show_image_offset(Image& someImage, int x, int y)
{
    //passthrough to avoid renaming
    showViewport(someImage, x, y);
}

void show_image_offset(Image& someImage, int x, int y)
{
    int w = someImage.width;
    int h = someImage.height;
    clear_display();
    for(int i=0; i<w; i++) {
            for(int j=0; j<h; j++) {
                    int dx = i + x;
                    int  dy = j + y;
                    if ( 0<=dx && dx <= 4 && 0<=dy && dy <= 4 ) {
                        display[dx][dy] = someImage.data[j*w + i ];
                    }
            }
    }
}

/* END - API IMPLEMENTATION ------------------------------------------------------------------*/