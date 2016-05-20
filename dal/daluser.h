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

#include "dalcore.h"

typedef struct Image {
    coord width;
    coord height;
    pixel *data ;
//    unsigned char *data;
} Image;

void eye_on(char id); // DONE
void eye_off(char id);// DONE

void eye_on(const char *id);// DONE
void eye_off(const char *id);// DONE

int getButton(const char *id);// DONE

void showViewport(Image& someImage, coord x, coord y);// DONE
void ScrollImage(Image someImage, boolean loop, int trailing_spaces);// DONE
pixel image_point(Image& someImage, coord x, coord y);// DONE
void set_image_point(Image& someImage, coord x, coord y, pixel value);// DONE

void print_message(const char * message, int pausetime);
void toggle_eye(char id);// DONE

struct StringImage;// DONE
void scroll_string_image(StringImage theSprite, int pausetime);// DONE

// Functions internal to the API
inline int image_point_index(Image& someImage, coord x, coord y);// DONE

void set_display(pixel sprite[5][5]) {
    for(coord i=0; i<5; i++) {
        for(coord j=0; j<5; j++) {
            set_point(i,j,sprite[i][j]);
        }
    }
}

inline int image_point_index(Image& someImage, coord x, coord y) {
   return x*someImage.width +y;
}

pixel image_point(Image& someImage, coord x, coord y) {
    if (x<0) return -1;
    if (y<0) return -2;
    if (x>someImage.width-1) return -1;
    if (x>someImage.height-1) return -2;
    return someImage.data[image_point_index(someImage, x, y)];
}

void set_image_point(Image& someImage, coord x, coord y, pixel value) {
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
        pause(pausetime);
    }
}
void print_message(char * message, int pausetime=100) {
    while(*message) {
        showLetter(*message);
        message++;
        pause(pausetime);
    }
}
void print_message(int number, int pausetime=100) {
    char num_buf[14];
    itoa(number, num_buf, 10);
    print_message(num_buf, 10);
}

void print_message(long number, int pausetime=100) {
    char num_buf[14];
    itoa(number, num_buf, 10);
    print_message(num_buf, 10);
}

void toggle_eye(char id) {
    if (get_eye(id) == HIGH) {
        set_eye(id, LOW);
    } else {
        set_eye(id, HIGH);
    }
}

void eye_on(char id) {
    set_eye(id, HIGH);
}

void eye_off(char id) {
    set_eye(id, LOW);
}

void showViewport(Image& someImage, coord x, coord y) {
    if (someImage.width<4) return; // Not implemented yet
    if (someImage.height<4) return; // Not implemented yet
    for(coord i=0; (i+x<someImage.width) && (i<5); i++) {
        for(coord j=y; (j+y<someImage.height) && (j<5); j++) {
            pixel value = someImage.data[(j+y)*someImage.width+ x+i ];
            set_point(i, j, value);
        }
    }
}

void ScrollImage(Image someImage, boolean loop=false, int trailing_spaces=false) {
    // Example, width is 16
    // Display width is 5
    // This counts from 0 <= i < 12 -- ie from 0 to 11
    // The last viewport therefore tries to display indices 11, 12, 13, 14, 15
    for(coord i=0; i<someImage.width-DISPLAY_WIDTH+1; i++) {
        clear_display();
        showViewport(someImage, i,0);
        pause(80);
    }
}

typedef struct StringImage {
    int mPixelPos;
    pixel mPixelData[50]; // Sufficient to hold two characters.
    char *mString;
    int mStrlen;
    char num_buf[12] ;

    StringImage() {}
    StringImage(const char * str) {
        setString(str);
    }
    StringImage(int number) {
        itoa(number, num_buf, 10);
        setString(num_buf);
    }
    StringImage(long number) {
        itoa(number, num_buf, 10);
        setString(num_buf);
    }
    ~StringImage() {}

    void setString(const char * str) {
        mString = (char *) str;
        mPixelPos = 0;
        for(int i=0; i<50; i++) {
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
        int first_char =0;
        int second_char =0;
        unsigned char first_char_data1[6];
        unsigned char second_char_data1[16];
        int char_index1;
        int char_index0;

        int vPixelPos = mPixelPos -5;

        if (vPixelPos <0) {
            first_char = 32;
            second_char = mString[0];
        } else {
            char_index0 = (vPixelPos / 5);
            char_index0 = char_index0 % mStrlen;
            char_index1 = (char_index0 +1) ;
            first_char = mString[char_index0];
            if (char_index1 < mStrlen) {
                char_index1 = char_index1 % mStrlen;
                second_char = mString[char_index1];
            }
        }

        for(int i=0; i<6; i++){
            first_char_data1[i] = get_font_data(first_char,i);
        }
        for(int i=0; i<6; i++){
            second_char_data1[i] = get_font_data(second_char,i);
        }

        for(int row=0; row<5; row++) {
            int row_first = first_char_data1[row + 1];
            int row_second = second_char_data1[row + 1];

            pixel F0 = 0b1000 & row_first ? HIGH : LOW;
            pixel F1 = 0b0100 & row_first ? HIGH : LOW;
            pixel F2 = 0b0010 & row_first ? HIGH : LOW;
            pixel F3 = 0b0001 & row_first ? HIGH : LOW;

            pixel S0 = 0b1000 & row_second ? HIGH : LOW;
            pixel S1 = 0b0100 & row_second ? HIGH : LOW;
            pixel S2 = 0b0010 & row_second ? HIGH : LOW;
            pixel S3 = 0b0001 & row_second ? HIGH : LOW;

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
} StringImage;

void scroll_string_image(StringImage theSprite, int pausetime=100) {
    for(int i=0; i<theSprite.pixel_width(); i++) {
        theSprite.render_string();
        theSprite.pan_right();
        pause(pausetime);
    }
}

void scroll_string(const char * str) {
    scroll_string_image(StringImage(str), 50);
}

void scroll_string(const char * str, int delay=100) {       // FIXME: Duplication
    scroll_string_image(StringImage(str), delay);
}

Image& _make_image(unsigned short int row1, unsigned short int row2, unsigned short int row3, unsigned short int row4, unsigned short int row5, int width) {
    unsigned short int rows[5];
    rows[0] = row5;
    rows[1] = row4;
    rows[2] = row3;
    rows[3] = row2;
    rows[4] = row1;

    Image* img = (Image*) malloc(sizeof(Image));
    img->width = width;
    img->height = 5;
    img->data = (pixel *) malloc(img->width * img->height * sizeof(pixel));

    pixel *pData = img->data;

    for(coord y=0; y < img->height; y++)
        for(coord x=0; x < img->width; x++)
            *pData++ = (rows[y] & (1<<x)) ? HIGH : LOW;
    Image& retVal = *img;
    return retVal;
}

Image& make_image(unsigned short int row1, unsigned short int row2, unsigned short int row3, unsigned short int row4, unsigned short int row5) {
    return _make_image(row1, row2, row3, row4, row5, 5);
}

Image& make_big_image(unsigned short int row1, unsigned short int row2, unsigned short int row3, unsigned short int row4, unsigned short int row5) {
    return _make_image(row1, row2, row3, row4, row5, 10);
}

void OLD_show_image_offset(Image& someImage, coord x, coord y) {
    //passthrough to avoid renaming
    showViewport(someImage, x, y);
}

// FIXME: Use plot/unplot - or perhaps "set point" - since more logical here
void show_image_offset(Image& someImage, coord x, coord y) {
    coord w = someImage.width;
    coord h = someImage.height;
    clear_display();
    for(coord i=0; i<w; i++) {
            for(coord j=0; j<h; j++) {
                    coord dx = i + x;
                    coord  dy = j + y;
                    if ( 0<=dx && dx <= 4 && 0<=dy && dy <= 4 ) {
                        set_point(dx, dy, someImage.data[j*w + i ]);
                    }
            }
    }
}

// -----------------------------------------------------------------------------------------------
//
// Compatibility thunks
//
int getButton(const char *id) { return getButton(*id); }
int getButton(char *id) { return getButton(*id); }
int get_button(char *id) { return getButton(*id); }
int get_button(const char *id) { return getButton(*id); }
int get_button(char id) { return getButton(id); }
pixel get_eye(char *id) { return get_eye(*id); }
pixel get_eye(const char *id) { return get_eye(*id); }
void showLetter(char * c) { showLetter(*c); }
void show_letter(char * c) { showLetter(*c); }
void show_letter(const char * c) { showLetter(*c); }
void show_letter(char c) { showLetter(c); }

void toggle_eye(const char *id){ toggle_eye(*id); }
void eye_on(const char *id) { set_eye(*id, HIGH); }
void eye_off(const char *id) { set_eye(*id, LOW); }
void set_eye(const char * id, pixel state) { set_eye(*id, state); }

/* END - API IMPLEMENTATION ------------------------------------------------------------------*/