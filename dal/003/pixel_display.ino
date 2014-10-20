#include "spark_font.h"

#define MICROBUG
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

int ButtonA = 15; // Arduino Pin for left eye
int ButtonB = 16; // Arduino Pin for left eye

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

int ButtonA = 15; // Arduino Pin for left eye
int ButtonB = 16; // Arduino Pin for left eye

#endif

int counter =0;
#define DELAY 5

int timer4_counter;

int display_strobe_counter;
int display[5][5] = {
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW}
                    };

/* API ---------------------------------------------------------------------------------------- */

#define DISPLAY_WIDTH 5
#define DISPLAY_HEIGHT 5

#define ___ 0

typedef struct Image {
    int width;
    int height;
    int *data ;
} Image;

void set_eye(char id, int state);
void eye_on(char id);
void eye_off(char id);
void print_message(char * message, int pausetime);
void showLetter(char c);
int getButton(char id);
void clear_display();
void plot(int x, int y);
void unplot(int x, int y);
int point(int x, int y);
void set_display(int sprite[5][5]);
void showViewport(Image& someImage, int x, int y);
void ScrollImage(Image someImage, boolean loop, int trailing_spaces);

void display_column(int i);
/* END API ------------------------------------------------------------------------------------ */


void setup_display() {
#ifdef MICROBUG

CLKPR = 0x80;
CLKPR = 0x01;
#endif

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

void microbug_setup() { // This is a really MicroBug setup
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

int image_point(Image& someImage, int x, int y) {
    if (x<0) return -1;
    if (y<0) return -2;
    if (x>someImage.width-1) return -1;
    if (x>someImage.height-1) return -2;

    return someImage.data[x*someImage.width +y ];
}

void clear_display() {
    for(int i=0; i< DISPLAY_WIDTH; i++) {
        for(int j=0; j< DISPLAY_HEIGHT; j++) {
            unplot(i,j);
        }
    }
}

int getButton(char id) {
    if (id == 'A') {
        return digitalRead(ButtonA);
    }
    if (id == 'B') {
        return digitalRead(ButtonB);
    }
    return -1; // Signify error
}

void showLetter(char c) {
    int letter_index = c-32;
    if (c>126) return;
    if (c<32) return;
    if (font[letter_index][0] != c) return;
    clear_display();
    for(int row=0; row<5; row++) {
        int this_row = font[letter_index][row+1];
        int L0 = 0b1000 & this_row ? HIGH : LOW;
        int L1 = 0b0100 & this_row ? HIGH : LOW;
        int L2 = 0b0010 & this_row ? HIGH : LOW;
        int L3 = 0b0001 & this_row ? HIGH : LOW;
        display[0][row] = L0;
        display[1][row] = L1;
        display[2][row] = L2;
        display[3][row] = L3;
        display[4][row] = LOW;
    }
}

void print_message(char * message, int pausetime) {
    while(*message) {
        showLetter(*message);
        message++;
        delay(pausetime);
    }
}

void set_eye(char id, int state) {
    if ((id == 'A') || (id == 'L')) {
        digitalWrite(lefteye, state );
    }
    if ((id == 'B') || (id == 'R')) {
        digitalWrite(righteye, state );
    }
}

void eye_on(char id) {
    set_eye(id, HIGH);
}

void eye_off(char id) {
    set_eye(id, LOW);
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
        delay(80);
    }
}

/* END - API IMPLEMENTATION ------------------------------------------------------------------*/

/* -- Test / application functions ---------------------------------------------------------- */
int cur_letter = 65;
void loop_letters() {
    showLetter(cur_letter);
    delay(500);
    cur_letter++;
    if (cur_letter>90) {
        cur_letter=65;
    }
}

void strobing_pixel_plot() {
   for(int i=0; i<5; i++) {
       for(int j=0; j<5; j++) {
           plot(i,j);
           delay(50); 
       }
   }
   for(int i=0; i<5; i++) {
       for(int j=0; j<5; j++) {
           unplot(i,j);
           delay(50); 
       }
   }
}

void checker_flash() {
    int checker_sprite[5][5] = {
                                  { HIGH, LOW, HIGH, LOW, HIGH },
                                  { LOW, HIGH, LOW, HIGH, LOW },
                                  { HIGH, LOW, HIGH, LOW, HIGH },
                                  { LOW, HIGH, LOW, HIGH, LOW },
                                  { HIGH, LOW, HIGH, LOW, HIGH }
                                };
    int inv_checker_sprite[5][5] = {
                                  { LOW, HIGH, LOW, HIGH, LOW },
                                  { HIGH, LOW, HIGH, LOW, HIGH },
                                  { LOW, HIGH, LOW, HIGH, LOW },
                                  { HIGH, LOW, HIGH, LOW, HIGH },
                                  { LOW, HIGH, LOW, HIGH, LOW }
                                };
    set_display(checker_sprite);
    digitalWrite(lefteye, HIGH);
    delay(500); 
    set_display(inv_checker_sprite);
    digitalWrite(lefteye, LOW);
    delay(500); 
}


void BasicBehaviours() {
    if ((getButton('A') == HIGH) && (getButton('B') == HIGH)) {
        loop_letters();
    } else if (getButton('A') == HIGH) {
        strobing_pixel_plot();
    } else if  (getButton('B') == HIGH) {
        checker_flash();
        clear_display();
    } else {
        eye_on('A');
        print_message("HELLO",200);
        eye_off('A');
        print_message(" WORLD!",200);
    }
}

Image myImage;
int image_data[] = {
    ___,  HIGH, ___,  ___,  ___,  ___,  HIGH, ___,  ___,  ___,  ___,  ___,  HIGH, ___,  ___,  ___,
    HIGH, ___, HIGH,  ___,  ___,  HIGH, ___,  HIGH, ___,  ___,  ___,  HIGH, ___,  HIGH, ___,  ___,
    ___,  ___,  HIGH, ___,  HIGH, ___,  ___,  HIGH, ___,  ___,  HIGH, ___,  ___,  HIGH, ___,  HIGH,
    ___,  HIGH, ___,  HIGH, ___,  ___,  ___,  ___,  HIGH, HIGH, ___,  ___,  ___,  ___,  HIGH, ___,
    HIGH, ___,  ___,  HIGH, ___,  ___,  ___,  ___,  HIGH, ___,  ___,  ___,  ___,  HIGH, HIGH, ___,
    ___,  ___,  ___,  ___,  HIGH, ___,  ___,  HIGH, ___,  HIGH, ___,  ___,  HIGH, ___,  ___,  HIGH,
    ___,  ___,  ___,  ___,  HIGH, ___,  HIGH, ___,  ___,  HIGH, ___,  HIGH, ___,  ___,  ___,  HIGH,
    HIGH, ___,  ___,  HIGH, ___,  HIGH, ___,  ___,  ___,  ___,  HIGH, ___,  ___,  ___,  ___,  ___
};

void FontSpriteTest_setup() {
    myImage.width=16;
    myImage.height=8;
    myImage.data = image_data;
}

void FontSpriteTest() {
    print_message("MICROBUG!",200);
    ScrollImage(myImage);
}


/* END  Test / application functions -------------------------------------------------------- */

void PixelReadTest_setup() {
    myImage.width=16;
    myImage.height=8;
    myImage.data = image_data;
    showViewport(myImage,0,0);
}

void PixelReadTest() {
}

int bootmode = 0;

void setup()
{
    setup_display();
    microbug_setup();
    if (digitalRead(ButtonA) == HIGH) {
        bootmode = 1;
    }
    if (bootmode == 1) {
        FontSpriteTest_setup();
    }
}

void loop()
{   
    if (bootmode == 1) {
        FontSpriteTest();
    } else {
        BasicBehaviours();
    }

}

