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
static void HW_Init(void);
void enable_power_optimisations();
void display_led(uint8_t x, uint8_t y);

// Common internal API functions
void check_bootkey();
void bootloader_start(void);

// Core API Functionality
void microbug_setup();
void pause(word millis);
void set_point(uint8_t x, uint8_t y, uint8_t state);
int point(int x, int y);
void plot(uint8_t x, uint8_t y);
void unplot(uint8_t x, uint8_t y);
int getButton(char id);
int get_eye(char id);
void set_eye(char id, int state);
unsigned char get_font_data(int ascii_value, int row);
void clear_display();
void showLetter(char c);

#define Usb_detach() (UDCON   |=  (1<<DETACH))

// --------------------------------------------------------------------------------------
// START Device level related defines

//Port B
#define LolRow4			7	//	0	o
#define LolDebug2		6	//	0	o
#define LolCol3			5	//	0	o
#define LolDebug1		4	//	0	o
// #define LolRightEye             3       //      0       o
#define	LolButtonB		2	//	0	i
//#define				1	//	0	i
#define	LolButtonA		0	//	0	i
#define	PORTB_INIT		0b00000000
#define	DDRB_INIT		0b11111000

#define LolDebug1H()	PORTB |= 1<<LolDebug1
#define LolDebug1L()	PORTB &= ~(1<<LolDebug1)
#define LolDebug2H()	PORTB |= 1<<LolDebug2
#define LolDebug2L()	PORTB &= ~(1<<LolDebug2)

#define LolRow4H()		PORTB |= 1<<LolRow4
#define LolRow4L()		PORTB &= ~(1<<LolRow4)
#define LolCol3H()		PORTB |= 1<<LolCol3
#define LolCol3L()		PORTB &= ~(1<<LolCol3)
// #define LolRightEyeH()  PORTB |= 1<<LolRightEye
// #define LolRightEyeL()  PORTB &= ~(1<<LolRightEye)

//Port C
#define LolCol4			7	//	0	o
#define	LolDebug3		6	//	0	o
//#define 				5	//	0	i
//#define 				4	//	0	i
//#define				3	//	0	i
//#define				2	//	0	i
//#define				1	//	0	i
//#define				0	//	0	i
#define	PORTC_INIT		0b00000000
#define	DDRC_INIT		0b11000000

#define LolDebug3H()	PORTC |= 1<<LolDebug3
#define LolDebug3L()	PORTC &= ~(1<<LolDebug3)

#define LolCol4H()		PORTC |= 1<<LolCol4
#define LolCol4L()		PORTC &= ~(1<<LolCol4)


//Port D
#define LolCol2			7	//	0	o
#define LolCol1			6	//	0	o
//#define 				5	//	0	i
#define LolCol0			4	//	0	o
#define	LolRow0			3	//	0	o
#define	LolRow1			2	//	0	o
#define	LolRow2			1	//	0	o
#define	LolRow3			0	//	0	o
#define	PORTD_INIT		0b00000000
#define	DDRD_INIT		0b11011111

#define LolRow0H()		PORTD |= 1<<LolRow0
#define LolRow0L()		PORTD &= ~(1<<LolRow0)
#define LolRow1H()		PORTD |= 1<<LolRow1
#define LolRow1L()		PORTD &= ~(1<<LolRow1)
#define LolRow2H()		PORTD |= 1<<LolRow2
#define LolRow2L()		PORTD &= ~(1<<LolRow2)
#define LolRow3H()		PORTD |= 1<<LolRow3
#define LolRow3L()		PORTD &= ~(1<<LolRow3)
#define LolCol0H()		PORTD |= 1<<LolCol0
#define LolCol0L()		PORTD &= ~(1<<LolCol0)
#define LolCol1H()		PORTD |= 1<<LolCol1
#define LolCol1L()		PORTD &= ~(1<<LolCol1)
#define LolCol2H()		PORTD |= 1<<LolCol2
#define LolCol2L()		PORTD &= ~(1<<LolCol2)


//Port E
//#define 				7	//	0	i
// #define LolLeftEye              6       //      0       o
//#define 				5	//	0	i
//#define 				4	//	0	i
//#define				3	//	0	i
#define	LolDebug4		2	//	0	o
//#define				1	//	0	i
//#define				0	//	0	i
#define	PORTE_INIT		0b00000000
#define	DDRE_INIT		0b01000100

#define LolDebug4H()    PORTE |= 1<<LolDebug4
#define LolDebug4L()    PORTE &= ~(1<<LolDebug4)

// #define LolLeftEyeH()   PORTE |= 1<<LolLeftEye
// #define LolLeftEyeL()   PORTE &= ~(1<<LolLeftEye)


#define LolLeftEye             3       //      0       o
#define LolLeftEyeH()  PORTB |= 1<<LolLeftEye
#define LolLeftEyeL()  PORTB &= ~(1<<LolLeftEye)

#define LolRightEye              6       //      0       o
#define LolRightEyeH()   PORTE |= 1<<LolRightEye
#define LolRightEyeL()   PORTE &= ~(1<<LolRightEye)

//Port F
#define LolCroc0		7	//	0	i
#define LolCroc1		6	//	0	i
#define LolCroc2		5	//	0	i
#define LolCroc3		4	//	0	i
//#define			3	//	0	i
//#define			2	//	0	i
#define	LolCroc4		1	//	0	i
#define	LolCroc5		0	//	0	i
#define	PORTF_INIT		0b00000000
#define	DDRF_INIT		0b00000000

//LolDebug
//#undef	DDRF_INIT
//#define	DDRF_INIT		0b11111111
//#define DEBUGSTATE(n)	PORTF = (PORTF & 0b00001111) | n<<4

//#define	LolDebug6		1	//	0	i
//#define	LolDebug5		0	//	0	i

//#define LolDebug5H()	PORTF |= 1<<LolDebug5
//#define LolDebug5L()	PORTF &= ~(1<<LolDebug5)
//#define LolDebug6H()	PORTF |= 1<<LolDebug6
//#define LolDebug6L()	PORTF &= ~(1<<LolDebug6)

#define power_timer4_enable() (PRR1 &= (uint8_t)~(1 << 4))
#define power_timer4_disable() (PRR1 |= (uint8_t)(1 << 4))


// Configure various aspects of hardware
const uint8_t TCCR3A_INIT = 0;
const uint8_t TCCR3B_RUN_VALUE = 0<<CS32 | 1<<CS31 | 1<<CS30;               // prescaler div 64
const uint8_t TCCR3B_STOP_VALUE = 0;
const uint16_t TCNT3_PRELOAD_VALUE = 65523;                                 // 65536-(2MHz/64*420us)
const uint8_t WDTCSR_INIT = 1<<WDIE | 0<<WDP2 | 0<<WDP1 | 0<<WDP0;          //  Interrupts only, 15ms
//const uint8_t WDTCSR_INIT = 1<<WDIE | 0<<WDP2 | 1<<WDP1 | 0<<WDP0;        //  Interrupts only, 60ms

// END - Device level related defines
// --------------------------------------------------------------------------------------

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

int ButtonA = 17; // Arduino Pin for left button // PIN 8    -- D17
int ButtonB = 16; // Arduino Pin for right button // PIN 10   -- D16

int croc0 = A0; // Arduino Pin crocodile clip 0 // PIN 36 -- A0
int croc1 = A1; // Arduino Pin crocodile clip 1 // PIN 37 -- A1
int croc2 = A2; // Arduino Pin crocodile clip 2 // PIN 38 -- A2
int croc3 = A3; // Arduino Pin crocodile clip 3 // PIN 39 -- A3
int croc4 = A4; // Arduino Pin crocodile clip 4 // PIN 40 -- A4
int croc5 = A5; // Arduino Pin crocodile clip 5 // PIN 41 -- A5

// This looks like it needs fixing, ALOT
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

int left_eye_state = HIGH; // Initial state is set to high in setup
int right_eye_state = HIGH; // Initial state is set to high in setup

uint8_t display[5][5] = {
                            { 0, 0, 0, 0, 0},
                            { 0, 0, 0, 0, 0},
                            { 0, 0, 0, 0, 0},
                            { 0, 0, 0, 0, 0},
                            { 0, 0, 0, 0, 0}
                        };

int dal_pre_pause_time = 1000; // Time to wait before starting the user program - allow the screen to settle
int dal_screen_hold_time = 500; // This is how long the display will hold for before going blank & sleeping after running
int sleep_time = 3; // This is the time in minutes before the device switches off
                     // Having it as a variable allows the user to override this.
long sleep_counter_t = 0;
long sleep_counter_t2 = 0;
volatile uint8_t UserTick = 0;


/*
void sleep(word millis) {
    Sleepy::loseSomeTime( millis);
}
*/

/* ------ START Power, display & device driving functions  ------------- */

static void HW_Init(void) {
    //ports:    direction and level (inc pullups)
    PORTB   = PORTB_INIT;   DDRB    = DDRB_INIT;
    PORTC   = PORTC_INIT;   DDRC    = DDRC_INIT;
    PORTD   = PORTD_INIT;   DDRD    = DDRD_INIT;
    PORTE   = PORTE_INIT;   DDRE    = DDRE_INIT;
    PORTF   = PORTF_INIT;   DDRF    = DDRF_INIT;
    //DIDR0 = DIDR0_INIT;
    //DIDR1 = DIDR1_INIT;
    //DIDR2 = DIDR2_INIT;

    //clock:
    CLKPR = 1<<CLKPCE;  CLKPR = 0b0010<<CLKPS0;     // 8MHz / 4 = 2MHz

    //timers:
    TCCR3B = TCCR3B_STOP_VALUE;
    TCNT3 = TCNT3_PRELOAD_VALUE;    // preload timer
    TCCR3A = TCCR3A_INIT;
    TCCR3B = TCCR3B_RUN_VALUE;
    TIMSK3 |= (1 << TOIE3);         // enable timer overflow interrupt

    MCUSR &= ~(1<<WDRF);            // Clear watchdog system reset flag
    WDTCSR |= (1<<WDCE) | (1<<WDE); // timed sequence
    WDTCSR = WDTCSR_INIT;

    // Disable JTAG - enable analogue input pins
    MCUCR |= (1 << JTD); MCUCR |= (1 << JTD);    //    Must be set twice in four cycles

}


// FIXME: Allow this to be granular
void enable_power_optimisations(){

//  power_adc_disable();  // FIXME: This needs to be more granular - though we've been running like this for 44 hours now though
    power_usart0_disable();
    power_spi_disable();
    power_twi_disable();
    power_timer1_disable();
    power_timer2_disable();
//  power_timer3_disable();
    power_timer4_disable();
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
    
    PLLFRQ |= 1<<PINMUX;

//  clock_prescale_set(clock_div_4);        // Switch the CPU speed right down.
}

ISR(WDT_vect)
{
    TCCR3B = TCCR3B_RUN_VALUE;
    set_sleep_mode(SLEEP_MODE_IDLE);
    UserTick++;
}


ISR(TIMER3_OVF_vect)
{
    static uint8_t display_led_x = 0;
    static uint8_t display_led_y = 0;

//LolDebug6H();
    TCNT3 = TCNT3_PRELOAD_VALUE;   // preload timer
    if(display_led_x < 5)
    {
        display_led(display_led_x,display_led_y);
        if(++display_led_y == 5)
        {
            display_led_y = 0;
            display_led_x++;
        }
    }
    else
    {
        switch(display_led_y++)
        {
        case 0:
            LolRow4L();
            LolCol4H();
            if(left_eye_state)      {           LolLeftEyeH();      }
            break;
        case 1:
            LolLeftEyeL();
            if(right_eye_state)     {           LolRightEyeH();     }
            break;
        default:
            LolRightEyeL();
            display_led_y = 0;
            display_led_x = 0;
            TCCR3B = TCCR3B_STOP_VALUE;
            set_sleep_mode(SLEEP_MODE_PWR_DOWN);
//DEBUGSTATE(0xE);
            break;  
        }
    }
//LolDebug6L();

    if (sleep_time > 0) {
        sleep_counter_t += 1;
        // One second == 1739?
        if (sleep_counter_t==52200) { // This is the number of times the display interrupt runs per 30 seconds, approximately.
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

void display_led(uint8_t x, uint8_t y) {

    LolCol0H();
    LolCol1H();
    LolCol2H();
    LolCol3H();
    LolCol4H();

    switch(y)
    {
    case 0:
        LolRow4L();
        if(display[x][0])   {   LolRow0H(); }
        break;
    case 1:
        LolRow0L();
        if(display[x][1])   {   LolRow1H(); }
        break;
    case 2:
        LolRow1L();
        if(display[x][2])   {   LolRow2H(); }
        break;
    case 3:
        LolRow2L();
        if(display[x][3])   {   LolRow3H(); }
        break;
    case 4:
        LolRow3L();
        if(display[x][4])   {   LolRow4H(); }
        break;
    default:
        break;
    }

    switch(x)   {
        case 0:     LolCol0L();     break;
        case 1:     LolCol1L();     break;
        case 2:     LolCol2L();     break;
        case 3:     LolCol3L();     break;
        case 4:     LolCol4L();     break;
        default:                    break;  }
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
    pause(200);
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

    HW_Init();

    digitalWrite(lefteye, HIGH);  // Turn status LEDs on prior to checking bootkey
    digitalWrite(righteye, HIGH); // If we reboot they will stay on.

    check_bootkey();              // This will never return if we reboot device.

    digitalWrite(lefteye, LOW);
    digitalWrite(righteye, LOW);

}

void pause(word millis) {
#ifdef MICROKIT_DISABLE
    delay(millis);
#else
    delay(millis/8);
#endif
}

// ---------------------------------------------------------------
//
// Functions for reading and updating device internal state
//
void set_point(uint8_t x, uint8_t y, uint8_t state) {
    if (x <0) return;
    if (x >DISPLAY_WIDTH-1) return;
    if (y <0) return;
    if (y >DISPLAY_HEIGHT -1) return;
    display[x][y] = state;
}

int point(int x, int y) {
    if (x <0) return -1;
    if (x >DISPLAY_WIDTH-1) return -1;
    if (y <0) return -2;
    if (y >DISPLAY_HEIGHT -1) return -2;
     return display[x][y];
}

void plot(uint8_t x, uint8_t y) {
    set_point(x,y,1);
}

void unplot(uint8_t x, uint8_t y) {
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
        left_eye_state = state;
    }
    if ((id == 'B') || (id == 'R') || (id == 'b') || (id == 'r')) {
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
    for(uint8_t i=0; i< DISPLAY_WIDTH; i++) {
        for(uint8_t j=0; j< DISPLAY_HEIGHT; j++) {
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
    for(int row=0; row<5; row++) {
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