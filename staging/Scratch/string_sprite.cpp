#include "spark_font.h"

#include <iostream>
#include <string.h>

// Simplistic test harness
#define ___ 0
#define HIGH 1
#define LOW 0

// This uses a struct rather than a class to flip the defaults to
// public rather than private or protected.

typedef struct StringSprite {
    int mPixelPos;
    int mPixelData[50]; // Sufficient to hold two characters.
    char *mString;
    int mStrlen;

    void setString(const char * str) {
        mString = (char *) str;
        mPixelPos = 0;
        for(int i=0; i++; i<50) {
            mPixelData[i] = 0;
        }
        mStrlen = strlen(mString);
    }

    void show_display() {
        int mPP = mPixelPos%5;
        for(int i=0; i<5; i++) {
            for(int j=0; j<5; j++) {
                std::cout << ( mPixelData[((i*10)+j+mPP)] == 0 ? " " : "#" );
            }
            std::cout << "|                            "<< std::endl;
        }
    }

    void show_buffer() {
        for(int i=0; i<5; i++) {
            for(int j=0; j<10; j++) {
                std::cout << ( mPixelData[((i*10)+j)] == 0 ? " " : "#" );
            }
            std::cout << "|                            "<< std::endl;
        }
    }
    void render_string(){
        // Renders into the pixel data buffer
        int first_char;
        int second_char;
        int char_index0 = (mPixelPos / 5) % mStrlen;
        int char_index1 = (char_index0 +1) % mStrlen;
        int *first_char_data;
        int *second_char_data;

        first_char = mString[char_index0];
        second_char = mString[char_index1];

        std::cout << ":" << char(first_char) << char(second_char) << ": ";
        std::cout << ">>" << first_char << ", " << second_char << "<< ";
        std::cout << mPixelPos << ", " << char_index0 << ", " << char_index1 << ", "<< mStrlen;
        std::cout << std::endl;

        first_char_data = font[first_char-32];
        second_char_data = font[second_char-32];

        for(int row=0; row<5; row++) {
            int row_first = first_char_data[row + 1];
            int row_second = second_char_data[row + 1];

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
//show_buffer();
show_display();


    }
    void pan_right() {
        // Move the viewport 1 pixel to the right. (Looks like scrolling left)
        mPixelPos += 1;
    }
    int pixel_width() {
        return mStrlen * 5;
    }
} StringSprite;

StringSprite myspr;



int main(int argc, char* argv[]) {

    myspr.setString("HELLO WORLD");

    for(int i=0; i<100; i++) {
        myspr.render_string();
        myspr.pan_right();
    }
    return 0;
}
