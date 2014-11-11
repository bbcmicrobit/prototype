var MKITJS = (function(){  

	// Cheat for now: font data here rather than using spark_font.json

	var font = [
				[32, 0, 0, 0, 0, 0],
				[33, 4, 4, 4, 0, 4],
				[34, 10, 10, 0, 0, 0],
				[35, 10, 15, 10, 15, 10],
				[36, 6, 13, 6, 11, 6],
				[37, 9, 2, 4, 9, 0],
				[38, 6, 4, 9, 6, 0],
				[39, 8, 8, 0, 0, 0],
				[40, 1, 2, 2, 2, 1],
				[41, 8, 4, 4, 4, 8],
				[42, 0, 10, 4, 10, 0],
				[43, 0, 4, 14, 4, 0],
				[44, 0, 0, 0, 4, 4],
				[45, 0, 0, 14, 0, 0],
				[46, 0, 0, 0, 4, 0],
				[47, 2, 2, 4, 8, 8],
				[48, 4, 10, 10, 10, 4],
				[49, 4, 12, 4, 4, 4],
				[50, 14, 1, 6, 8, 15],
				[51, 15, 1, 2, 9, 6],
				[52, 8, 10, 10, 15, 2],
				[53, 15, 8, 6, 1, 14],
				[54, 7, 8, 14, 9, 14],
				[55, 15, 1, 2, 4, 4],
				[56, 6, 9, 6, 9, 6],
				[57, 7, 9, 7, 1, 1],
				[58, 0, 4, 0, 4, 0],
				[59, 0, 4, 0, 4, 4],
				[60, 1, 2, 4, 2, 1],
				[61, 0, 14, 0, 14, 0],
				[62, 4, 2, 1, 2, 4],
				[63, 6, 9, 2, 0, 6],
				[64, 7, 11, 11, 8, 6],
				[65, 6, 9, 9, 15, 9],
				[66, 14, 9, 14, 9, 14],
				[67, 7, 8, 8, 8, 7],
				[68, 14, 9, 9, 9, 14],
				[69, 15, 8, 14, 8, 15],
				[70, 15, 8, 14, 8, 8],
				[71, 7, 8, 11, 9, 7],
				[72, 9, 9, 15, 9, 9],
				[73, 14, 4, 4, 4, 14],
				[74, 15, 1, 1, 9, 6],
				[75, 9, 10, 12, 10, 9],
				[76, 8, 8, 8, 8, 15],
				[77, 9, 15, 15, 15, 9],
				[78, 9, 13, 11, 11, 9],
				[79, 6, 9, 9, 9, 6],
				[80, 14, 9, 14, 8, 8],
				[81, 6, 9, 9, 6, 3],
				[82, 14, 9, 14, 9, 9],
				[83, 7, 8, 6, 1, 14],
				[84, 7, 2, 2, 2, 2],
				[85, 9, 9, 9, 9, 6],
				[86, 9, 9, 9, 10, 4],
				[87, 9, 11, 15, 15, 9],
				[88, 9, 9, 6, 9, 9],
				[89, 9, 5, 2, 4, 8],
				[90, 15, 2, 4, 8, 15],
				[91, 3, 2, 2, 2, 3],
				[92, 4, 4, 2, 1, 1],
				[93, 12, 4, 4, 4, 12],
				[94, 4, 10, 0, 0, 0],
				[95, 0, 0, 0, 0, 15],
				[96, 4, 2, 0, 0, 0],
				[97, 0, 7, 9, 7, 0],
				[98, 8, 14, 9, 14, 0],
				[99, 0, 7, 8, 7, 0],
				[100, 1, 7, 9, 7, 0],
				[101, 6, 9, 14, 7, 0],
				[102, 3, 4, 14, 4, 0],
				[103, 0, 15, 9, 15, 15],
				[104, 8, 14, 9, 9, 0],
				[105, 6, 0, 6, 6, 0],
				[106, 2, 0, 4, 4, 8],
				[107, 8, 11, 14, 9, 0],
				[108, 4, 4, 4, 6, 0],
				[109, 0, 14, 11, 11, 0],
				[110, 0, 12, 10, 10, 0],
				[111, 0, 6, 9, 6, 0],
				[112, 0, 14, 9, 14, 8],
				[113, 0, 7, 9, 7, 1],
				[114, 0, 3, 4, 4, 0],
				[115, 0, 3, 6, 14, 0],
				[116, 4, 6, 4, 2, 0],
				[117, 0, 9, 9, 7, 0],
				[118, 0, 9, 10, 4, 0],
				[119, 0, 9, 11, 6, 0],
				[120, 0, 9, 6, 9, 0],
				[121, 0, 9, 13, 2, 12],
				[122, 0, 15, 4, 15, 0],
				[123, 3, 2, 6, 2, 3],
				[124, 4, 4, 4, 4, 4],
				[125, 12, 4, 6, 4, 12],
				[126, 5, 10, 0, 0, 0]
	];

	// Constants
	var DISPLAY_WIDTH = 5;
	var DISPLAY_HEIGHT = 5;
	var HIGH = 1;
	var LOW = 0;
	var PRESSED = HIGH;

	// Microkit Constants
	var row0 = 1; // Arduino Pin for row 4 // PIN 21 -- D1
	var row1 = 0; // Arduino Pin for row 3  // PIN 20 -- D0
	var row2 = 2; // Arduino Pin for row 2  // PIN 19 -- D2
	var row3 = 3; // Arduino Pin for row 1  // PIN 18 -- D3
	var row4 = 11; // Arduino Pin for row 0 // PIN 12 -- D11

	var col0 = 4; // Arduino Pin for row 0  // PIN 25 -- D4
	var col1 = 12; // Arduino Pin for row 1  // PIN 26 -- D12
	var col2 = 6; // Arduino Pin for row 2  // PIN 27 -- D6
	var col3 = 9; // Arduino Pin for row 3 // PIN 29 -- D9
	var col4 = 13; // Arduino Pin for row 4  // PIN 32 -- D13

	var lefteye = 7; // Arduino Pin for left eye // PIN 1     -- D7
	var righteye = 14; // Arduino Pin for left eye // PIN 11  -- D14

	var ButtonA = 17; // Arduino Pin for left eye // PIN 8    -- D17
	var ButtonB = 16; // Arduino Pin for left eye // PIN 10   -- D16    

	// State 
	var display = [
		[LOW, LOW, LOW, LOW, LOW],
		[LOW, LOW, LOW, LOW, LOW],
		[LOW, LOW, LOW, LOW, LOW],
		[LOW, LOW, LOW, LOW, LOW],
		[LOW, LOW, LOW, LOW, LOW]
	];

	var pins = [];
	var left_eye_state;


	////////////////////////////////////////////////////////////////
	// Simulator implementation

	function Image()
	{
		var width;
		var height;
		var data; //int*
	};

	function digitalWrite(pin, state)
	{
		pins[pin] = state;
	}

	function digitalRead(pin)
	{
		var pinVal = pins[pin];
		if (pinVal === undefined)
			console.log("digitalRead addressing undefined pin");

		return pins[pin];   
	}

	function bootloader_start(){}

	function check_bootkey() {
		if (digitalRead(ButtonA) == PRESSED) {
			bootloader_start();
		}
	}	

	////////////////////////////////////////////////////////////////
	// Abstraction Layer Internals

	function image_point_index(someImage, x ,y) {
		return x*someImage.width +y;
	}

	function display_column(i) {
		digitalWrite(col0, HIGH);
		digitalWrite(col1, HIGH);
		digitalWrite(col2, HIGH);
		digitalWrite(col3, HIGH);
		digitalWrite(col4, HIGH);

		digitalWrite(row0, display[i][0] );
		digitalWrite(row1, display[i][1] );
		digitalWrite(row2, display[i][2] );
		digitalWrite(row3, display[i][3] );
		digitalWrite(row4, display[i][4] );

		if (i == 0) digitalWrite(col0, LOW );
		if (i == 1) digitalWrite(col1, LOW );
		if (i == 2) digitalWrite(col2, LOW );
		if (i == 3) digitalWrite(col3, LOW );
		if (i == 4) digitalWrite(col4, LOW );
	}

	function setup_display()
	{

	}

	function microbug_setup()
	{  
		setup_display();
		//     display_strobe_counter = 0;
		//     pinMode(row0, OUTPUT);
		//     pinMode(row1, OUTPUT);
		//     pinMode(row2, OUTPUT);
		//     pinMode(row3, OUTPUT);
		//     pinMode(row4, OUTPUT);
		//     pinMode(col0, OUTPUT);
		//     pinMode(col1, OUTPUT);
		//     pinMode(col2, OUTPUT);
		//     pinMode(col3, OUTPUT);
		//     pinMode(col4, OUTPUT);
		//     pinMode(lefteye, OUTPUT);
		//     pinMode(righteye, OUTPUT);
		//     pinMode(ButtonA, INPUT);
		//     pinMode(ButtonB, INPUT);
		digitalWrite(row0, LOW);
		digitalWrite(row1, LOW);
		digitalWrite(row2, LOW);
		digitalWrite(row3, LOW);
		digitalWrite(row4, LOW);

		digitalWrite(col0, HIGH);
		digitalWrite(col1, HIGH);
		digitalWrite(col2, HIGH);
		digitalWrite(col3, HIGH);
		digitalWrite(col4, HIGH);

		digitalWrite(lefteye, HIGH);
		digitalWrite(righteye, HIGH);
	}


	////////////////////////////////////////////////////////////////
	// API implementation

	var set_eye = function(cId, iState)
	{
		if ((id == 'A') || (id == 'L')) {
			digitalWrite(lefteye, state );
			left_eye_state = state;
		}
		if ((id == 'B') || (id == 'R')) {
			digitalWrite(righteye, state );
			right_eye_state = state;
		}
	};

	var eye_on = function (cId) {
		set_eye(cId, HIGH);
	};

	var eye_off = function(cId) {
		set_eye(cId, LOW);
	};

	var print_message = function(message, pausetime) {
		console.log("print_message TBD");
		//     while(*message) {
		//         showLetter(*message);
		//         message++;
		//         delay(pausetime);
		//     }
	};

	var showLetter = function(c) {
		var letter_index = c-32;
		if (c>126) return;
		if (c<32) return;

		if (font[letter_index][0] != c) return;

		clear_display();

		for(var row=0; row<5; row++) {
			var this_row = font[letter_index][row+1];
			var L0 = 8 & this_row ? HIGH : LOW;
			var L1 = 4 & this_row ? HIGH : LOW;
			var L2 = 2 & this_row ? HIGH : LOW;
			var L3 = 1 & this_row ? HIGH : LOW;
			display[0][row] = L0;
			display[1][row] = L1;
			display[2][row] = L2;
			display[3][row] = L3;
			display[4][row] = LOW;
		}
	};

	var getButton = function(id) {
		if (id == 'A') {
			return digitalRead(ButtonA);
		}
		if (id == 'B') {
			return digitalRead(ButtonB);
		}
		return -1; // Signify error
	};

	var clear_display = function()
	{
		for(var i=0; i< DISPLAY_WIDTH; i++) {
			for(var j=0; j< DISPLAY_HEIGHT; j++) {
				unplot(i,j);
			}
		}
	};

	var plot = function(x, y) {
		if (x <0) return;
		if (x >DISPLAY_WIDTH-1) return;

		if (y <0) return;
		if (y >DISPLAY_HEIGHT -1) return;

		 display[x][y] = HIGH;
	};

	var unplot = function(x, y) {
		if (x <0) return;
		if (x >DISPLAY_WIDTH-1) return;

		if (y <0) return;
		if (y >DISPLAY_HEIGHT -1) return;

		 display[x][y] = LOW;
	};

	var point = function(x, y) {
		// Bounds checking
		if (x <0) return -1;
		if (x >DISPLAY_WIDTH-1) return -1;

		if (y <0) return -2;
		if (y >DISPLAY_HEIGHT -1) return -2;

		return display[x][y];
	};

//  var set_display = function(int sprite[5][5]) {
	var set_display = function(sprite) {
		for(var i=0; i<5; i++) {
			for(var j=0; j<5; j++) {
				display[i][j] = sprite[i][j];
			}
		}
	};

//    void showViewport(Image& someImage, int x, int y) {
	var showViewport = function(someImage, x, y) {
		if (someImage.width<4) return; // Not implemented yet
		if (someImage.height<4) return; // Not implemented yet
		for(var i=0; (i+x<someImage.width) && (i<5); i++) {
			for(var j=y; (j+y<someImage.height) && (j<5); j++) {
				var value = someImage.data[(j+y)*someImage.width+ x+i ];
				display[i][j]=value;
			}
		}
	};

	var ScrollImage = function(someImage, loop, trailing_spaces)
	{
		loop = loop || false;
		trailing_spaces = trailing_spaces || false;
		console.log("ScrollImage TBD");
		// for(var i=0; i<someImage.width-DISPLAY_WIDTH+1; i++) {
		//     clear_display();
		//     showViewport(someImage, i,0);
		//     delay(80);
		// }
	};

	var image_point = function(someImage, x, y) {
		if (x<0) return -1;
		if (y<0) return -2;
		if (x>someImage.width-1) return -1;
		if (x>someImage.height-1) return -2;
		return someImage.data[image_point_index(someImage, x, y)];
	};

	var set_image_point = function(someImage, x, y, value) {
		if (x<0);
		if (y<0);
		if (x>someImage.width-1);
		if (x>someImage.height-1);

		someImage.data[image_point_index(someImage, x, y)] = value;
	};

	var toggle_eye = function(id) {
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
	};

	return {
		set_eye : set_eye,
		eye_on : eye_on,
		eye_off : eye_off,
		print_message : print_message,
		showLetter : showLetter,
		getButton : getButton,
		clear_display : clear_display,
		plot : plot,
		unplot : unplot,
		point : point,
		set_display : set_display,
		showViewport : showViewport,
		ScrollImage : ScrollImage,
		image_point : image_point,
		set_image_point : set_image_point,
		toggle_eye : toggle_eye
	};
})();

//TBD
//struct StringSprite;
//void scroll_sprite(StringSprite theSprite, int pausetime);

// typedef struct StringSprite {
//     int mPixelPos;
//     int mPixelData[50]; // Sufficient to hold two characters.
//     char *mString;
//     int mStrlen;

//     StringSprite() {}
//     StringSprite(const char * str) {
//         setString(str);
//     }
//     ~StringSprite() {}

//     void setString(const char * str) {
//         mString = (char *) str;
//         mPixelPos = 0;
//         for(int i=0; i++; i<50) {
//             mPixelData[i] = 0;
//         }
//         mStrlen = strlen(mString);
//     }

//     void update_display() {
//         Image myImage;
//         int mPP = mPixelPos%5;
//         myImage.width=10;
//         myImage.height=5;
//         myImage.data = mPixelData;
//         showViewport(myImage, mPP,0);

//     }
//     void render_string(){
//         // Renders into the pixel data buffer
//         int first_char;
//         int second_char;
// //         unsigned char *first_char_data;
// //         unsigned char *second_char_data;

//         unsigned char first_char_data1[6];
//         unsigned char second_char_data1[16];
//         int char_index1;

//         int char_index0 = (mPixelPos / 5);

//         char_index0 = char_index0 % mStrlen;

//         first_char = mString[char_index0];
//         for(int i=0; i<6; i++){
//             first_char_data1[i] = pgm_read_byte(&(font[first_char-32][i]));
//         }

//         char_index1 = (char_index0 +1) ;
//         if (char_index1 < mStrlen) {
//             char_index1 = char_index1 % mStrlen;
//             second_char = mString[char_index1];
// //            second_char_data = (unsigned char*) ( font[second_char-32] );

//             for(int i=0; i<6; i++){
//                 second_char_data1[i] = pgm_read_byte(&(font[second_char-32][i]));
//             }
//         } else {
// //            second_char_data =  (unsigned char*) ( font[0] );
//             for(int i=0; i<6; i++){
//                 second_char_data1[i] = pgm_read_byte(&(font[0][i]));
//             }
//         }

//         for(int row=0; row<5; row++) {
//             int row_first = first_char_data1[row + 1];
//             int row_second = second_char_data1[row + 1];

//             int F0 = 0b1000 & row_first ? HIGH : LOW;
//             int F1 = 0b0100 & row_first ? HIGH : LOW;
//             int F2 = 0b0010 & row_first ? HIGH : LOW;
//             int F3 = 0b0001 & row_first ? HIGH : LOW;

//             int S0 = 0b1000 & row_second ? HIGH : LOW;
//             int S1 = 0b0100 & row_second ? HIGH : LOW;
//             int S2 = 0b0010 & row_second ? HIGH : LOW;
//             int S3 = 0b0001 & row_second ? HIGH : LOW;

//             mPixelData[0+row*10] = F0;
//             mPixelData[1+row*10] = F1;
//             mPixelData[2+row*10] = F2;
//             mPixelData[3+row*10] = F3;
//             mPixelData[4+row*10] = 0;

//             mPixelData[5+row*10] = S0;
//             mPixelData[6+row*10] = S1;
//             mPixelData[7+row*10] = S2;
//             mPixelData[8+row*10] = S3;
//             mPixelData[9+row*10] = 0;
//         }
//         update_display();
//     }
//     void pan_right() {
//         // Move the viewport 1 pixel to the right. (Looks like scrolling left)
//         mPixelPos += 1;
//         if (mPixelPos>=pixel_width()) {
//             mPixelPos =0;
//         }
//     }
//     int pixel_width() {
//         return mStrlen * 5;
//     }
// } StringSprite;

// void scroll_sprite(StringSprite theSprite, int pausetime=100) {
//     for(int i=0; i<theSprite.pixel_width(); i++) {
//         theSprite.render_string();
//         theSprite.pan_right();
//         delay(pausetime);
//     }
// }

// void scroll_string(const char * str) {
//     scroll_sprite(StringSprite(str), 50);
// }
// void scroll_string(const char * str, int delay) {
//     scroll_sprite(StringSprite(str), delay);
// }


