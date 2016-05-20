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

#include "daluser.h"
#include <math.h>

void sleep(int time) { pause(time); }         // POWER
int sum(int a, int b, int c) { return a+b+c; } // COMPILER SUPPORT

auto x = 0;

void setup()
{
    microbug_setup();
}

void user_program()
{
    // TBD - setting a variable to None is not supported - to simplify variable type tracing;
    long last = 0;

    sleep_counter_t = 0;
    sleep_counter_t2 = 0;

    print_message(last,400);

    while(true) {
        if (sleep_counter_t2 != last) {
            last = sleep_counter_t2;
            print_message(last,400);
        }
        pause(10);
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
        pause(2000);
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


