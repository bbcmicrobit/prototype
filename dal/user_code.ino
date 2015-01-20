#include "dal.h"
#include <math.h>

// ISR(WDT_vect) { Sleepy::watchdogEvent(); } // POWER
void sleep(int time) { pause(time); }         // POWER
int dal_screen_hold_time = 500;               // POWER
// int get_button(char *button) { return getButton(*button); } // POWER
// int get_button(const char *button) { return getButton(*button); } // POWER
int sleep_time = 1;                // POWER
void set_eye(const char* eye,int state) { set_eye(*eye, state); }// POWER
int sum(int a, int b, int c) { return a+b+c; } // COMPILER SUPPORT
void scroll_string(char * some_string, int delay=100) { scroll_string_image(StringImage(some_string),delay); } // COMPILER TEST SUITE SUPPORT



auto x = 0;

void setup()
{
    microbug_setup();
}

void user_program()
{
    // TBD - setting a variable to None is not supported - to simplify variable type tracing;
    if (get_eye("A")) {
        x = 0;
        for(int x=5; x>-1; x= x + -2) {
          plot( x,0 );
          pause( 1000 );
        };
    }
}

int main(void)
{
        init();

#if defined(USBCON)
//        USBDevice.attach();
#endif
        setup(); // Switches on "eyes", and switches to bootloader if required
        enable_power_optimisations();
set_eye('L', LOW);  // Switch off eyes if bootloader not required
set_eye('R', LOW);
        user_program();
        //        if (serialEventRun) serialEventRun();
        if (dal_screen_hold_time) { 
            pause(dal_screen_hold_time);
            clear_display();
            eye_off("A");
            eye_off("B");
            while (true) {
                sleep(1000);
            }
            return 0;
        } else {
            while(1) {
                pause(dal_screen_hold_time);
                }
        }
}


