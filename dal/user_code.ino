

#include "dal.h"

unsigned long time;
unsigned long lasttime;
int buttondown;
ISR(WDT_vect) { Sleepy::watchdogEvent(); }


void ScrollSpriteStringSpriteExample_Test18() {
    auto merry = StringImage("Test");

    set_eye('L', HIGH);
    set_eye('R', HIGH);
    scroll_string_image(merry, 50);
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
//    int time = sleep_time ; //millis();

    for(int i=5; i>-1; i--) {
        print_message(i,100);
        pause(1000);
    }
   long time = sleep_counter_t2 ; //millis();

   scroll_string_image(StringImage(time), 100);
   scroll_string_image(StringImage("##"), 100);
}


int main(void)
{
        init();

#if defined(USBCON)
        USBDevice.attach();
#endif
        setup();
        enable_power_optimisations();
        sleep_time = 5;
        for (;;) {
                loop();
                if (serialEventRun) serialEventRun();
        }
        return 0;
}
