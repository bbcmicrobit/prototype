
#include "dal.h"

#include <CommandHostTiny.h>

class TetherHost : public CommandHostTiny {
private:

  char temp_str[128];
public:
  TetherHost()  { }
  ~TetherHost() { }

  const char *hostid() { 
    return "testhosttiny";
  }

  const char * attrs() {
    return "";
  }
  const char * funcs() {
    return "eyeon,eyeoff,scrollstring";
  }

  bool has_help(char * name) {

    if (strcmp(name,"eyeon")==0) return true;
    if (strcmp(name,"eyeoff")==0) return true;
    if (strcmp(name,"scrollstring")==0) return true;

    return false;
  }

  void help(char * name) {

    if (strcmp(name,"eyeon")==0) Serial.println(F("eyeon myarg:str -> - Switch eye on L or R"));
    else if (strcmp(name,"eyeoff")==0) Serial.println(F("eyeoff myarg:str -> - Switch eye off L or R"));
    else if (strcmp(name,"scrollstring")==0) Serial.println(F("scrollstring myarg:str -> - Scroll a message"));

    else Serial.println(F("-"));
  }

  bool exists(char * attribute) {
    return false;
  }

  const char *get(char * attribute) {
    return "-";
  }

  int set(char* attribute, char* raw_value) {
    return 404;
  }

  int one_arg_int_result_int(char *raw_value) {
      int value = atoi(raw_value);
      itoa (value, result_string, 10);
      return 200;
  }
  void eyeon(char *raw_value) {
    eye_on(*raw_value);
  }
  void eyeoff(char *raw_value) {
    eye_off(*raw_value);
  }
  void scrollstring(char *raw_value){
    scroll_string(raw_value,100);
  }

  int callfunc(char* funcname, char* raw_args) { 
    // Since this is a test host, it doesn't actually do anything
    if (strcmp(funcname,"eyeon")==0) { eyeon(raw_args); return 200; }
    if (strcmp(funcname,"eyeoff")==0) { eyeoff(raw_args); return 200; }
    if (strcmp(funcname,"scrollstring")==0)  { scrollstring(raw_args); return 200; }

    return 200;
  }

  void setup(void) {
      // Setup the pins
      CommandHostTiny::setup();
  }
};

TetherHost MyCommandHost;




unsigned long time;
unsigned long lasttime;
int buttondown;

void setup()
{    //.These next three should be merged into one
    microbug_setup();
    lasttime = 0;
    time = 0;
    buttondown = 0;
set_eye('L', HIGH);
set_eye('R', HIGH);

  MyCommandHost.setup();

}

void loop()
{
    MyCommandHost.run_host();
}

int main(void)
{
        init();

#if defined(USBCON)
        USBDevice.attach();
#endif
set_eye('L', LOW);
set_eye('R', LOW);
        setup();
// set_eye('R', LOW);
        for (;;) {
                loop();
                if (serialEventRun) serialEventRun();
        }
        return 0;
}
