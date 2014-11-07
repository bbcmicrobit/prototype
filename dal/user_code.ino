
#include "dal.h"

unsigned long time;
unsigned long lasttime;
int buttondown;

void ScrollSpriteStringSpriteExample_Test18() {
    scroll_sprite(StringSprite("HELLO WORLD"),50);
    delay(70);
    scroll_sprite(StringSprite(":-) (:)"),50);
    print_message("* * ", 100);
    while(1) {
        if (getButton('A') == PRESSED) break;
        if (getButton('B') == PRESSED) {
            buttondown = 1;
        } else {
            if (buttondown == 1) { // Button released -- may be nice to wrap this up
                time = millis();
                if (time-lasttime > 10) { // Debounce
                    toggle_eye('A');
                    toggle_eye('B');
                    lasttime = time;
                    buttondown = 0;
                }
            }
        }
        delay(50);
    }
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
set_eye('L', LOW);
set_eye('R', LOW);
// set_eye('R', LOW);
        for (;;) {
                loop();
                if (serialEventRun) serialEventRun();
        }
        return 0;
}
