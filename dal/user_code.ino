
#include "dal.h"

void ScrollSpriteStringSpriteExample_Test18() {
    while(1) {
        if (getButton('A') == PRESSED) break;
        delay(50);
    }
    scroll_sprite(StringSprite("HELLO WORLD"),50);
    delay(70);
    scroll_sprite(StringSprite(":-) (:)"),50);
    print_message("* * ", 100);
}

void setup()
{    //.These next three should be merged into one
    microbug_setup();
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
        for (;;) {
                loop();
                if (serialEventRun) serialEventRun();
        }
        return 0;
}
