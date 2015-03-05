
#include "dalcore.h"

typedef struct Image {
    int width;
    int height;
    int *data ;
} Image;

void set_eye(char id, int state);
void eye_on(char id);
void eye_off(char id);
void print_message(const char * message, int pausetime);
void showViewport(Image& someImage, int x, int y);
void ScrollImage(Image someImage, boolean loop, int trailing_spaces);
int image_point(Image& someImage, int x, int y);
void set_image_point(Image& someImage, int x, int y, int value);
void print_message(const char * message, int pausetime);
void toggle_eye(char id);

struct StringSprite;
void scroll_sprite(StringSprite theSprite, int pausetime);

// Functions internal to the API
inline int image_point_index(Image& someImage, int x, int y);


// Crutch during development
void scroll_string(const char * str); // FIXME: Crutch during development
void scroll_string(const char * str, int delay); // FIXME: Crutch during development

//----
void eye_on(char id);
void eye_off(char id);
void print_message(const char * message, int pausetime);
void showViewport(Image& someImage, int x, int y);

void ScrollImage(Image someImage, boolean loop, int trailing_spaces);
int image_point(Image& someImage, int x, int y);
void set_image_point(Image& someImage, int x, int y, int value);
void toggle_eye(char id);

struct StringSprite;
void scroll_sprite(StringSprite theSprite, int pausetime);

// Functions internal to the API
inline int image_point_index(Image& someImage, int x, int y);

// Crutch during development
void scroll_string(const char * str); // FIXME: Crutch during development
void scroll_string(const char * str, int delay); // FIXME: Crutch during development
//----




inline int image_point_index(Image& someImage, int x, int y) {
   return x*someImage.width +y;
}

int image_point(Image& someImage, int x, int y) {
    if (x<0) return -1;
    if (y<0) return -2;
    if (x>someImage.width-1) return -1;
    if (x>someImage.height-1) return -2;

    return someImage.data[image_point_index(someImage, x, y)];
}

void set_image_point(Image& someImage, int x, int y, int value) {
    if (x<0);
    if (y<0);
    if (x>someImage.width-1);
    if (x>someImage.height-1);

    someImage.data[image_point_index(someImage, x, y)] = value;
}

void print_message(const char * message, int pausetime=100) {
    while(*message) {
        showLetter(*message);
        message++;
        delay(pausetime);
    }
}

void toggle_eye(char id) {
    if ((id == 'A') || (id == 'L')) {
        if (left_eye_state == HIGH) {
            set_eye(id, LOW);
        } else {
            set_eye(id, HIGH);
        }
    }
    if ((id == 'B') || (id == 'R')) {
        if (right_eye_state == HIGH) {
            set_eye(id, LOW);
        } else {
            set_eye(id, HIGH);
        }
    }
}

void eye_on(char id) {
    set_eye(id, HIGH);
}

void eye_off(char id) {
    set_eye(id, LOW);
}

void showViewport(Image& someImage, int x, int y) {
    if (someImage.width<4) return; // Not implemented yet
    if (someImage.height<4) return; // Not implemented yet
    for(int i=0; (i+x<someImage.width) && (i<5); i++) {
        for(int j=y; (j+y<someImage.height) && (j<5); j++) {
            int value = someImage.data[(j+y)*someImage.width+ x+i ];
            display[i][j]=value;
        }
    }
}

void ScrollImage(Image someImage, boolean loop=false, int trailing_spaces=false) {
    // Example, width is 16
    // Display width is 5
    // This counts from 0 <= i < 12 -- ie from 0 to 11
    // The last viewport therefore tries to display indices 11, 12, 13, 14, 15
    for(int i=0; i<someImage.width-DISPLAY_WIDTH+1; i++) {
        clear_display();
        showViewport(someImage, i,0);
        delay(80);
    }
}

typedef struct StringSprite {
    int mPixelPos;
    int mPixelData[50]; // Sufficient to hold two characters.
    char *mString;
    int mStrlen;

    StringSprite() {}
    StringSprite(const char * str) {
        setString(str);
    }
    ~StringSprite() {}

    void setString(const char * str) {
        mString = (char *) str;
        mPixelPos = 0;
        for(int i=0; i++; i<50) {
            mPixelData[i] = 0;
        }
        mStrlen = strlen(mString);
    }

    void update_display() {
        Image myImage;
        int mPP = mPixelPos%5;
        myImage.width=10;
        myImage.height=5;
        myImage.data = mPixelData;
        showViewport(myImage, mPP,0);

    }
    void render_string(){
        // Renders into the pixel data buffer
        int first_char;
        int second_char;
//         unsigned char *first_char_data;
//         unsigned char *second_char_data;

        unsigned char first_char_data1[6];
        unsigned char second_char_data1[16];
        int char_index1;

        int char_index0 = (mPixelPos / 5);

        char_index0 = char_index0 % mStrlen;

        first_char = mString[char_index0];
        for(int i=0; i<6; i++){
            first_char_data1[i] = pgm_read_byte(&(font[first_char-32][i]));
        }

        char_index1 = (char_index0 +1) ;
        if (char_index1 < mStrlen) {
            char_index1 = char_index1 % mStrlen;
            second_char = mString[char_index1];
//            second_char_data = (unsigned char*) ( font[second_char-32] );

            for(int i=0; i<6; i++){
                second_char_data1[i] = pgm_read_byte(&(font[second_char-32][i]));
            }
        } else {
//            second_char_data =  (unsigned char*) ( font[0] );
            for(int i=0; i<6; i++){
                second_char_data1[i] = pgm_read_byte(&(font[0][i]));
            }
        }

        for(int row=0; row<5; row++) {
            int row_first = first_char_data1[row + 1];
            int row_second = second_char_data1[row + 1];

            int F0 = 0b1000 & row_first ? HIGH : LOW;
            int F1 = 0b0100 & row_first ? HIGH : LOW;
            int F2 = 0b0010 & row_first ? HIGH : LOW;
            int F3 = 0b0001 & row_first ? HIGH : LOW;

            int S0 = 0b1000 & row_second ? HIGH : LOW;
            int S1 = 0b0100 & row_second ? HIGH : LOW;
            int S2 = 0b0010 & row_second ? HIGH : LOW;
            int S3 = 0b0001 & row_second ? HIGH : LOW;

            mPixelData[0+row*10] = F0;
            mPixelData[1+row*10] = F1;
            mPixelData[2+row*10] = F2;
            mPixelData[3+row*10] = F3;
            mPixelData[4+row*10] = 0;

            mPixelData[5+row*10] = S0;
            mPixelData[6+row*10] = S1;
            mPixelData[7+row*10] = S2;
            mPixelData[8+row*10] = S3;
            mPixelData[9+row*10] = 0;
        }
        update_display();
    }
    void pan_right() {
        // Move the viewport 1 pixel to the right. (Looks like scrolling left)
        mPixelPos += 1;
        if (mPixelPos>=pixel_width()) {
            mPixelPos =0;
        }
    }
    int pixel_width() {
        return mStrlen * 5;
    }
} StringSprite;

void scroll_sprite(StringSprite theSprite, int pausetime=100) {
    for(int i=0; i<theSprite.pixel_width(); i++) {
        theSprite.render_string();
        theSprite.pan_right();
        delay(pausetime);
    }
}

void scroll_string(const char * str) {
    scroll_sprite(StringSprite(str), 50);
}
void scroll_string(const char * str, int delay) {
    scroll_sprite(StringSprite(str), delay);
}

/* END - API IMPLEMENTATION ------------------------------------------------------------------*/
