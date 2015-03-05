
//  include "dal.h"
#include "daluser.h"

#include <CommandHostTiny.h>

class TetherHost : public CommandHostTiny {
private:

  char temp_str[128];
public:
  TetherHost()  { }
  ~TetherHost() { }

  const char *hostid() { 
    return "microbug";
  }

  const char * attrs() {
    return "";
  }
  const char * funcs() {
    return "eyeon,eyeoff,scrollstring,getbutton,plot,unplot,cleardisplay";
  }

  bool has_help(char * name) {

    if (strcmp(name,"eyeon")==0) return true;
    if (strcmp(name,"eyeoff")==0) return true;
    if (strcmp(name,"scrollstring")==0) return true;
    if (strcmp(name,"getbutton")==0) return true;
    if (strcmp(name,"plot")==0) return true;
    if (strcmp(name,"unplot")==0) return true;
    if (strcmp(name,"cleardisplay")==0) return true;

    return false;
  }

  void help(char * name) {

    if (strcmp(name,"eyeon")==0) Serial.println(F("eyeon myarg:str -> - Switch eye on L or R"));
    else if (strcmp(name,"eyeoff")==0) Serial.println(F("eyeoff myarg:str -> - Switch eye off L or R"));
    else if (strcmp(name,"scrollstring")==0) Serial.println(F("scrollstring myarg:str -> - Scroll a message"));
    else if (strcmp(name,"getbutton")==0) Serial.println(F("scrollstring myarg:str -> result:int - get button state - A or B"));
    else if (strcmp(name,"plot")==0) Serial.println(F("plot intlist:str -> - Light up a pixel at x,y - x,y is treated as a string for the moment"));
    else if (strcmp(name,"unplot")==0) Serial.println(F("unplot intlist:str -> - Light up a pixel at x,y - x,y is treated as a string for the moment"));
    else if (strcmp(name,"cleardisplay")==0) Serial.println(F("cleardisplay -> - Clear the display"));

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
    scroll_string(raw_value,50);
  }
  void getbutton(char *raw_value) {
      int value = getButton(*raw_value);
      itoa (value, result_string, 10);
  }
  void com_plot(char *raw_value) {
      int x,y;
      char *raw_y;
      char *pos = strstr(raw_value, ",");
      char *raw_x = raw_value; // Yes, we mean to point raw_x at the same thing as raw_value
      raw_y = pos;
      raw_y++;
      *pos = 0;
      x = atoi(raw_x);
      y = atoi(raw_y);

      plot(x,y);
  }

  void com_unplot(char *raw_value) {
      int x,y;
      char *raw_y;
      char *pos = strstr(raw_value, ",");
      char *raw_x = raw_value; // Yes, we mean to point raw_x at the same thing as raw_value
      raw_y = pos;
      raw_y++;
      *pos = 0;
      x = atoi(raw_x);
      y = atoi(raw_y);

      unplot(x,y);
  }
  void cleardisplay(char *raw_value) {
      clear_display();
  }

  int callfunc(char* funcname, char* raw_args) { 
    // Since this is a test host, it doesn't actually do anything
    if (strcmp(funcname,"eyeon")==0) { eyeon(raw_args); return 200; }
    if (strcmp(funcname,"eyeoff")==0) { eyeoff(raw_args); return 200; }
    if (strcmp(funcname,"scrollstring")==0)  { scrollstring(raw_args); return 200; }
    if (strcmp(funcname,"getbutton")==0)  { getbutton(raw_args); return 200; }
    if (strcmp(funcname,"plot")==0)  { com_plot(raw_args); return 200; }
    if (strcmp(funcname,"unplot")==0)  { com_unplot(raw_args); return 200; }
    if (strcmp(funcname,"cleardisplay")==0)  { com_unplot(raw_args); return 200; }

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
