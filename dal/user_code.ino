
#include "dal.h"

unsigned long time;
unsigned long lasttime;
int buttondown;
ISR(WDT_vect) { Sleepy::watchdogEvent(); }


void ScrollSpriteStringSpriteExample_Test18() {
    int count;

    set_eye('L', HIGH);
    set_eye('R', HIGH);
    scroll_string_image(StringImage(" MERRY XMAS!"),50);
    sleep(30);
    set_eye('L', LOW);
    set_eye('R', LOW);


    count = 0;
    while (count < 30) {
        count = count +1;
        sleep(30);
        if (getButton('A') == PRESSED) 
            break;
    }

    set_eye('L', HIGH);
    set_eye('R', HIGH);
    scroll_string_image(StringImage(" MERRY XMAS"),50);
    sleep(300);

    set_eye('L', LOW);
    set_eye('R', LOW);


    count = 0;
    while (count < 300) {
        count = count +1;
        sleep(50);
        if (getButton('A') == PRESSED) 
            break;
    }


    set_eye('L', HIGH);
    set_eye('R', HIGH);
    scroll_string_image(StringImage(" NOW BRING US SOME FIGGY PUDDING"),50);
    sleep(300);
    set_eye('L', LOW);
    set_eye('R', LOW);


    count = 0;
    while (count < 30) {
        count = count +1;
        sleep(50);
        if (getButton('A') == PRESSED) 
            break;
    }

    set_eye('L', HIGH);
    set_eye('R', HIGH);
    scroll_string_image(StringImage(" AND A HAPPY NEW YEAR!"),50);
    sleep(300);

    set_eye('L', LOW);
    set_eye('R', LOW);


    count = 0;
    while (count < 3000) {
        count = count +1;
        sleep(50);
        if (getButton('A') == PRESSED) 
            break;
        if (count == 100)  {
            set_eye('L', HIGH);
            set_eye('R', HIGH);
        }
        if (count == 130) {
            set_eye('L', LOW);
            set_eye('R', LOW);
        }

        if (count == 700)  {
            set_eye('L', HIGH);
        }
        if (count == 710) {
            set_eye('L', LOW);
        }

        if (count == 1400)  {
            set_eye('R', HIGH);
        }
        if (count == 1410) {
            set_eye('R', LOW);
        }
        if (count == 1410) {
            scroll_string_image(StringImage(" DO I DO EVERYTHING ROUND HERE?"),50);
        }

        if (count == 2100)  {
            set_eye('L', HIGH);
            set_eye('R', HIGH);
        }
        if (count == 2110) {
            set_eye('L', LOW);
            set_eye('R', LOW);
        }
    }

//    scroll_string_image(StringImage(":-) (:)"),50);
//    print_message("* * ", 100);
//    while(1) {
//        if (getButton('A') == PRESSED) break;
//        if (getButton('B') == PRESSED) {
//            buttondown = 1;
//        } else {
//            if (buttondown == 1) { // Button released -- may be nice to wrap this up
//                time = millis();
//                if (time-lasttime > 10) { // Debounce
//                    toggle_eye('A');
//                    toggle_eye('B');
//                    lasttime = time;
//                    buttondown = 0;
//                }
//            }
//        }
//        sleep(50);
//    }
}

void setup()
{    //.These next three should be merged into one
    microbug_setup();
    lasttime = 0;
    time = 0;
    buttondown = 0;
}

void loop()
{
    ScrollSpriteStringSpriteExample_Test18();
}


int main(void)
{
        init();

#if defined(USBCON)
        USBDevice.attach();
#endif
        setup();
        enable_power_optimisations();
        for (;;) {
                loop();
                if (serialEventRun) serialEventRun();
        }
        return 0;
}
