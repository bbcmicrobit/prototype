
#define MICROBUG
#ifdef MEGABUG
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
#endif


#ifdef MICROBUG

int row0 = 12; // Arduino Pin for row 0
int row1 = 4; // Arduino Pin for row 1
int row2 = 2; // Arduino Pin for row 2
int row3 = 3; // Arduino Pin for row 3
int row4 = 11; // Arduino Pin for row 4

int col0 = 6; // Arduino Pin for row 0
int col1 = 8; // Arduino Pin for row 1
int col2 = 9; // Arduino Pin for row 2
int col3 = 10; // Arduino Pin for row 3
int col4 = 5; // Arduino Pin for row 4

int lefteye = 7; // Arduino Pin for left eye
int righteye = 17; // Arduino Pin for left eye

int ButtonA = 15; // Arduino Pin for left eye
int ButtonB = 16; // Arduino Pin for left eye
#endif

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

void all_on() {
      digitalWrite(row0, HIGH);
      digitalWrite(row1, HIGH);
      digitalWrite(row2, HIGH);
      digitalWrite(row3, HIGH);
      digitalWrite(row4, HIGH);
      digitalWrite(col0, LOW);
      digitalWrite(col1, LOW);
      digitalWrite(col2, LOW);
      digitalWrite(col3, LOW);
      digitalWrite(col4, LOW);
}

void all_off() {
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
}


void iterate_rows() {
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

      digitalWrite(row0, HIGH);
  delay(DELAY);
      digitalWrite(row0, LOW);

      digitalWrite(row1, HIGH);
  delay(DELAY);
      digitalWrite(row1, LOW);

      digitalWrite(row2, HIGH);
  delay(DELAY);
      digitalWrite(row2, LOW);

      digitalWrite(row3, HIGH);
  delay(DELAY);
      digitalWrite(row3, LOW);

      digitalWrite(row4, HIGH);
  delay(DELAY);
      digitalWrite(row4, LOW);

}

void iterate_cols() {
      digitalWrite(col0, HIGH);
      digitalWrite(col1, HIGH);
      digitalWrite(col2, HIGH);
      digitalWrite(col3, HIGH);
      digitalWrite(col4, HIGH);

      digitalWrite(row0, HIGH);
      digitalWrite(row1, HIGH);
      digitalWrite(row2, HIGH);
      digitalWrite(row3, HIGH);
      digitalWrite(row4, HIGH);

      digitalWrite(col0, LOW);
  delay(DELAY);
      digitalWrite(col0, HIGH);

      digitalWrite(col1, LOW);
  delay(DELAY);
      digitalWrite(col1, HIGH);

      digitalWrite(col2, LOW);
  delay(DELAY);
      digitalWrite(col2, HIGH);

      digitalWrite(col3, LOW);
  delay(DELAY);
      digitalWrite(col3, HIGH);

      digitalWrite(col4, LOW);
  delay(DELAY);
      digitalWrite(col4, HIGH);


}

void pixels() {

      digitalWrite(row0, HIGH); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, LOW); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, HIGH); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, LOW ); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, HIGH); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, LOW ); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, HIGH); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, LOW ); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, HIGH); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, LOW );
  delay(DELAY);

// -------------------
      digitalWrite(row0, LOW ); digitalWrite(row1, HIGH); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, LOW ); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, HIGH); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, LOW ); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, HIGH); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, LOW ); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, HIGH); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, LOW ); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, HIGH); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, LOW );
  delay(DELAY);

// --------------------
      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, HIGH); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, LOW ); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, HIGH); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, LOW ); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, HIGH); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, LOW ); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, HIGH); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, LOW ); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, HIGH); digitalWrite(row3, LOW ); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, LOW );
  delay(DELAY);
// ----------------------
      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, HIGH); digitalWrite(row4, LOW );
      digitalWrite(col0, LOW ); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, HIGH); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, LOW ); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, HIGH); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, LOW ); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, HIGH); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, LOW ); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, HIGH); digitalWrite(row4, LOW );
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, LOW );
  delay(DELAY);
// ----------------------
      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, HIGH);
      digitalWrite(col0, LOW); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, HIGH);
      digitalWrite(col0, HIGH); digitalWrite(col1, LOW ); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, HIGH);
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, LOW ); digitalWrite(col3, HIGH); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, HIGH);
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, LOW ); digitalWrite(col4, HIGH);
  delay(DELAY);

      digitalWrite(row0, LOW ); digitalWrite(row1, LOW ); digitalWrite(row2, LOW ); digitalWrite(row3, LOW ); digitalWrite(row4, HIGH);
      digitalWrite(col0, HIGH); digitalWrite(col1, HIGH); digitalWrite(col2, HIGH); digitalWrite(col3, HIGH); digitalWrite(col4, LOW );
  delay(DELAY);



}

void blink_eyes() {
  digitalWrite(lefteye,HIGH);
  digitalWrite(righteye,HIGH);
  delay(200);
  digitalWrite(lefteye,LOW);
  digitalWrite(righteye,LOW);
}

void loop() {
    int button_a = digitalRead(ButtonA);
    int button_b = digitalRead(ButtonB);

    if (button_a && button_b) {
      all_on();
      delay(100);
      all_off();
      delay(100);
    } else if (button_a) {
        iterate_rows();
    } else if (button_b) {
        iterate_cols();
    } else {
        pixels();
//        blink_eyes();
    }
}














