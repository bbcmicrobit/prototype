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

void setup()
{
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

void pixels() {
      int display[5][5] = {
                            { HIGH, LOW, HIGH, LOW, HIGH },
                            { LOW, HIGH, LOW, HIGH, LOW },
                            { HIGH, LOW, HIGH, LOW, HIGH },
                            { LOW, HIGH, LOW, HIGH, LOW },
                            { HIGH, LOW, HIGH, LOW, HIGH }
                          };

      for(int i=0; i<5; i++) {
      
          digitalWrite(row0, display[i][0] ); digitalWrite(row1, display[i][1] ); digitalWrite(row2, display[i][2]); digitalWrite(row3, display[i][3] ); digitalWrite(row4, display[i][4] );
          digitalWrite(col0, i != 0 ? HIGH : LOW );
          digitalWrite(col1, i != 1 ? HIGH : LOW );
          digitalWrite(col2, i != 2 ? HIGH : LOW );
          digitalWrite(col3, i != 3 ? HIGH : LOW );
          digitalWrite(col4, i != 4 ? HIGH : LOW );
      delay(DELAY);
      }
}

void pixels_2() {
      int display[5][5] = {
                            { LOW, HIGH, LOW, HIGH, LOW },
                            { HIGH, LOW, HIGH, LOW, HIGH },
                            { LOW, HIGH, LOW, HIGH, LOW },
                            { HIGH, LOW, HIGH, LOW, HIGH },
                            { LOW, HIGH, LOW, HIGH, LOW }
                          };

      for(int i=0; i<5; i++) {
      
          digitalWrite(row0, display[i][0] ); digitalWrite(row1, display[i][1] ); digitalWrite(row2, display[i][2]); digitalWrite(row3, display[i][3] ); digitalWrite(row4, display[i][4] );
          digitalWrite(col0, i != 0 ? HIGH : LOW );
          digitalWrite(col1, i != 1 ? HIGH : LOW );
          digitalWrite(col2, i != 2 ? HIGH : LOW );
          digitalWrite(col3, i != 3 ? HIGH : LOW );
          digitalWrite(col4, i != 4 ? HIGH : LOW );
      delay(DELAY);
      }
}



void loop() {
   
    int button_a = digitalRead(ButtonA);
    int button_b = digitalRead(ButtonB);
    counter += 1;

    if (counter > 50) {
        pixels_2();
        if (counter > 100){
           counter = 0;
        }
    } else {
       pixels();
    }
   
}














