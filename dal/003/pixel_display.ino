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

int counter =0;
#define DELAY 5


#define ledPin 7
int timer4_counter;

int mycounter;
int display[5][5] = {
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW},
                      { LOW, LOW, LOW, LOW, LOW}
                    };

void mySetup() {
      mycounter = 0;
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

      digitalWrite(col0, LOW);
      digitalWrite(col1, LOW);
      digitalWrite(col2, LOW);
      digitalWrite(col3, LOW);
      digitalWrite(col4, LOW);

      digitalWrite(lefteye, LOW);
      digitalWrite(righteye, LOW);
}


void setup()
{
  mySetup();
  pinMode(ledPin, OUTPUT);

  // initialize timer4 
  noInterrupts();           // disable all interrupts
  TCCR4A = 0;
  TCCR4B = 0;

  // Set timer4_counter to the correct value for our interrupt interval
  timer4_counter = 64911;     // preload timer 65536-16MHz/256/100Hz
  timer4_counter = 65224;     // preload timer 65536-16MHz/256/200Hz

  TCNT4 = timer4_counter;   // preload timer
  TCCR4B |= (1 << CS12);    // 256 prescaler 
  TIMSK4 |= (1 << TOIE4);   // enable timer overflow interrupt
  interrupts();             // enable all interrupts
}

void display_column(int i) {
    digitalWrite(row0, display[i][0] ); digitalWrite(row1, display[i][1] ); digitalWrite(row2, display[i][2]); digitalWrite(row3, display[i][3] ); digitalWrite(row4, display[i][4] );
    digitalWrite(col0, i != 0 ? HIGH : LOW );
    digitalWrite(col1, i != 1 ? HIGH : LOW );
    digitalWrite(col2, i != 2 ? HIGH : LOW );
    digitalWrite(col3, i != 3 ? HIGH : LOW );
    digitalWrite(col4, i != 4 ? HIGH : LOW );
}


ISR(TIMER4_OVF_vect)        // interrupt service routine 
{
  TCNT4 = timer4_counter;   // preload timer

  display_column(mycounter % 5);

  mycounter += 1;
  if (mycounter > 200) {
    mycounter = 0; // reset
  }
}

void set_display(int sprite[5][5]) {
    for(int i=0; i<5; i++) {
        for(int j=0; j<5; j++) {
           display[i][j] = sprite[i][j];
        }
    }
}

#define DISPLAY_WIDTH 5
#define DISPLAY_HEIGHT 5

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

void clear_display() {
    for(int i=0; i< DISPLAY_WIDTH; i++) {
        for(int j=0; j< DISPLAY_HEIGHT; j++) {
            unplot(i,j);
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
    digitalWrite(ledPin, HIGH);
    delay(500); 
    set_display(inv_checker_sprite);
    digitalWrite(ledPin, LOW);
    delay(500); 
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

void loop()
{
    strobing_pixel_plot();
}
