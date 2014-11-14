var DALJS = (function(){  

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
	var right_eye_state;

	//var blocking = true;
	var blocking = false;

	////////////////////////////////////////////////////////////////
	// Simulator implementation

	var printMessageStr = "";
	var printMessageInterval;

	var imageToScroll;
	var imageScrollInterval;
	var imageScrollOffsetH;

	var spriteToScroll;
	var spriteScrollInterval;
	var spriteScrollOffsetH;

	function Image()
	{
		var width;
		var height;
		var data; //int*
	}

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

	function bootloaderStart(){}

	function checkBootKey() {
		if (digitalRead(ButtonA) == PRESSED) {
			bootloaderStart();
		}
	}

	function delay(ms)
	{
		var start = new Date().getTime();
		for (var i = 0; i < 1e7; i++) {
			if ((new Date().getTime() - start) > ms)
			{
				console.log(".");
				break;
			}
		}
    }

	function handlePrintMessage()
	{
		if (blocking)
		{
			while (printMessageStr.length)
			{
				showLetter(printMessageStr[0]);
				printMessageStr = printMessageStr.substr(1);
				delay(printMessageInterval);				
			}
		}
		else
		{
			showLetter(printMessageStr[0]);
			printMessageStr = printMessageStr.substr(1);

			if (printMessageStr.length)
				setTimeout(handlePrintMessage, printMessageInterval);
		}
	}

	function handleScrollImage()
	{
		if (blocking)
		{
			while (imageScrollOffsetH < imageToScroll.width-DISPLAY_WIDTH+1)
			{
				clearDisplay();
				showViewport(imageToScroll, imageScrollOffsetH, 0);
				imageScrollOffsetH++;
				delay(imageScrollInterval);
			}	
		}
		else
		{
			clearDisplay();
			showViewport(imageToScroll, imageScrollOffsetH, 0);

			if (imageScrollOffsetH < imageToScroll.width-DISPLAY_WIDTH+1)
			{
				imageScrollOffsetH++;
				setTimeout(handleScrollImage, imageScrollInterval);
			}
		}
	}

	function handleScrollSprite()
	{
		if (blocking)
		{
			while(spriteScrollOffsetH < spriteToScroll.pixel_width())
			{
				spriteToScroll.render_string();
				spriteToScroll.pan_right();
				spriteScrollOffsetH++;
				delay(spriteScrollInterval);				
			}
		}
		else
		{
			if (spriteScrollOffsetH < spriteToScroll.pixel_width())
			{
				spriteToScroll.render_string();
				spriteToScroll.pan_right();
				spriteScrollOffsetH++;
				setTimeout(handleScrollSprite, spriteScrollInterval);
			}
		}
	}

	function dirty()
	{
		if (dirtyCallback)
			dirtyCallback(display, [left_eye_state, right_eye_state]);
	}

	////////////////////////////////////////////////////////////////
	// Abstraction Layer Internals

	function imagePointIndex(someImage, x ,y) {
		return x*someImage.width +y;
	}

	////////////////////////////////////////////////////////////////
	// API implementation

	var setEye = function(id, state)
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

	var eyeOn = function (cId) {
		setEye(cId, HIGH);
	};

	var eyeOff = function(cId) {
		setEye(cId, LOW);
	};

	var printMessage = function(message, pausetime) {
		printMessageStr = message;
		printMessageInterval = pausetime | 100;
		handlePrintMessage();
	};

	var showLetter = function(c) {

		if (typeof(c) === "string")
		{
			c = c.charCodeAt(0);
		}

		var letter_index = c-32;
		if (c>126) return;
		if (c<32) return;

		if (font[letter_index][0] != c) return;

		clearDisplay();

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

		dirty();
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

	var clearDisplay = function()
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

		dirty();
	};

	var unplot = function(x, y) {
		if (x <0) return;
		if (x >DISPLAY_WIDTH-1) return;

		if (y <0) return;
		if (y >DISPLAY_HEIGHT -1) return;

		display[x][y] = LOW;

		dirty();
	};

	var point = function(x, y) {
		// Bounds checking
		if (x <0) return -1;
		if (x >DISPLAY_WIDTH-1) return -1;

		if (y <0) return -2;
		if (y >DISPLAY_HEIGHT -1) return -2;

		return display[x][y];
	};

//  var setDisplay = function(int sprite[5][5]) {
	var setDisplay = function(sprite) {
		for(var i=0; i<5; i++) {
			for(var j=0; j<5; j++) {
				display[i][j] = sprite[i][j];
			}
		}
		dirty();
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
		dirty();
	};

	var scrollImage = function(someImage, loop, trailing_spaces)
	{
		//NOT YET USED
		//loop = loop || false;
		//trailing_spaces = trailing_spaces || false;

		imageToScroll = someImage;
		imageScrollInterval = 80;
		imageScrollOffsetH = 0;

		handleScrollImage();
	};

	var imagePoint = function(someImage, x, y) {
		if (x<0) return -1;
		if (y<0) return -2;
		if (x>someImage.width-1) return -1;
		if (x>someImage.height-1) return -2;
		return someImage.data[imagePointIndex(someImage, x, y)];
	};

	var setImagePoint = function(someImage, x, y, value) {
		if (x<0);
		if (y<0);
		if (x>someImage.width-1);
		if (x>someImage.height-1);

		someImage.data[imagePointIndex(someImage, x, y)] = value;
	};

	var toggleEye = function(id) {
		if ((id == 'A') || (id == 'L')) {
			if (left_eye_state == HIGH) {
				setEye(id, LOW);
			} else {
				setEye(id, HIGH);
			}
		}
		if ((id == 'B') || (id == 'R')) {
			if (right_eye_state == HIGH) {
				setEye(id, LOW);
			} else {
				setEye(id, HIGH);
			}
		}
	};

	function StringSprite(str) {
		this.mPixelPos = 0;
		this.mPixelData = []; // was [50] Sufficient to hold two characters.
		this.mString = "";
		this.mStrlen = 0;

		if(str !== undefined)
			this.setString(str);
	}

	StringSprite.prototype.setString = function(str)
	{
		this.mString = str;
		this.mPixelPos = 0;
		for(var i=0; i++; i<50) {
			this.mPixelData[i] = 0;
		}
		this.mStrlen = this.mString.length;
	};

	StringSprite.prototype.update_display = function()
	{
		var myImage = new Image();
		var mPP = this.mPixelPos%5;
		myImage.width = 10;
		myImage.height = 5;
		myImage.data = this.mPixelData;
		showViewport(myImage, mPP, 0);
	};

	StringSprite.prototype.render_string = function() {
		var i;

		var first_char;
		var second_char;
		var first_char_data;
		var second_char_data;

		var first_char_data1 = [];//6
		var second_char_data1 = [];//16
		var char_index1;

		var char_index0 = Math.floor(this.mPixelPos / 5); //GOTCHA!
		char_index0 = char_index0 % this.mStrlen;

		first_char = this.mString[char_index0];
		for(i = 0; i < 6; i++){
			first_char_data1[i] = font[first_char.charCodeAt(0)-32][i];
		}

		char_index1 = (char_index0 + 1);
		if (char_index1 < this.mStrlen) {
			char_index1 = char_index1 % this.mStrlen;
			second_char = this.mString[char_index1];

			for(i=0; i<6; i++){
				second_char_data1[i] = font[second_char.charCodeAt(0)-32][i];
			}
		} else {
			for(i=0; i<6; i++){
				second_char_data1[i] = font[0][i];
			}
		}

		for(var row=0; row<5; row++) {
			var row_first = first_char_data1[row + 1];
			var row_second = second_char_data1[row + 1];

			var F0 = 8 & row_first ? HIGH : LOW;
			var F1 = 4 & row_first ? HIGH : LOW;
			var F2 = 2 & row_first ? HIGH : LOW;
			var F3 = 1 & row_first ? HIGH : LOW;

			var S0 = 8 & row_second ? HIGH : LOW;
			var S1 = 4 & row_second ? HIGH : LOW;
			var S2 = 2 & row_second ? HIGH : LOW;
			var S3 = 1 & row_second ? HIGH : LOW;

			this.mPixelData[0+row*10] = F0;
			this.mPixelData[1+row*10] = F1;
			this.mPixelData[2+row*10] = F2;
			this.mPixelData[3+row*10] = F3;
			this.mPixelData[4+row*10] = 0;

			this.mPixelData[5+row*10] = S0;
			this.mPixelData[6+row*10] = S1;
			this.mPixelData[7+row*10] = S2;
			this.mPixelData[8+row*10] = S3;
			this.mPixelData[9+row*10] = 0;
		}
		this.update_display();
	};

	StringSprite.prototype.pan_right = function() {
		this.mPixelPos += 1;
		if (this.mPixelPos>=this.pixel_width()) {
			this.mPixelPos = 0;
		}
	};

	StringSprite.prototype.pixel_width = function() {
		return this.mStrlen * 5;
	};

	var scrollSprite = function(theSprite, delay)
	{
		delay = delay || 100;
		spriteToScroll = theSprite;
		spriteScrollInterval = delay;
		spriteScrollOffsetH = 0;
		handleScrollSprite();
	};

	var scrollString = function(str, delay)
	{
		delay = delay || 50;
		scrollSprite(new StringSprite(str), delay);
	};

	var debug = function()
	{
		var rowString = "";
		for(var i = 0; i < DISPLAY_HEIGHT; i++) {
			for (var j = 0; j < DISPLAY_WIDTH; j++) {
				if (display[j][i] === HIGH)
					rowString+= "*";
				else
					rowString+= " ";
			}
			rowString+="\n";
		}
		console.log(rowString);
	};

	var getDisplay = function()
	{
		return display;
	};

	var setDirtyCallback= function(fn) {
		dirtyCallback = fn;
	};

	return {
		setEye : setEye,
		eyeOn : eyeOn,
		eyeOff : eyeOff,
		printMessage : printMessage,
		showLetter : showLetter,
		getButton : getButton,
		clearDisplay : clearDisplay,
		plot : plot,
		unplot : unplot,
		point : point,
		setDisplay : setDisplay,
		showViewport : showViewport,
		scrollImage : scrollImage,
		imagePoint : imagePoint,
		setImagePoint : setImagePoint,
		toggleEye : toggleEye,
		scrollSprite: scrollSprite,
		scrollString: scrollString,

		debug:debug,
		getDisplay:getDisplay,
		setDirtyCallback:setDirtyCallback
	};
})();