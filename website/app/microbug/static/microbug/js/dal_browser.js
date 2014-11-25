var DALJS = (function(){  

	// Constants
	var DISPLAY_WIDTH = 5;
	var DISPLAY_HEIGHT = 5;
	var HIGH = 1;
	var LOW = 0;
	var PRESSED = HIGH;

	// State 
	var display = [
		[LOW, LOW, LOW, LOW, LOW],
		[LOW, LOW, LOW, LOW, LOW],
		[LOW, LOW, LOW, LOW, LOW],
		[LOW, LOW, LOW, LOW, LOW],
		[LOW, LOW, LOW, LOW, LOW]
	];
	var left_eye_state;
	var right_eye_state;

	////////////////////////////////////////////////////////////////
	// Simulator implementation

	var printMessageStr = "";
	var printMessageInterval;

	var imageToScroll;
	var imageScrollInterval;
	var imageScrollOffsetH;
	var imageToScrollW = 0;
	var imageToScrollH = 0;


	var scrollSpriteOffset;

	var micro_device_ready = true;
	var dirtyCallback;

	function deviceReady() {
		return micro_device_ready;
	}

	function Image(imageData)
	{
//		console.log("Image dal_browser constructor");
		if (imageData)
		{
			this.data = imageData;
			this.height = imageData.length;
			this.width = imageData[0].length;		
		}
		else
		{
			this.data = null;
			this.height = 0;
			this.width = 0;
		}
	}

	function daldirty()
	{
		if (dirtyCallback)
			dirtyCallback(display, [left_eye_state, right_eye_state]);
	}

	var clearDisplay = function()
	{
		var unplot = function(x, y) {
			if (x <0) return;
			if (x >DISPLAY_WIDTH-1) return;

			if (y <0) return;
			if (y >DISPLAY_HEIGHT -1) return;

			display[x][y] = LOW;

			daldirty();
		};

		for(var i=0; i< DISPLAY_WIDTH; i++) {
			for(var j=0; j< DISPLAY_HEIGHT; j++) {
				unplot(i,j);
			}
		}
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

		daldirty();
	};

	var showViewportStringSprite = function(someImage, x, y)
	{
		//someImage.data is a flat array for strings;
		for(var i=0; (i+x<someImage.width) && (i<5); i++) {
			for(var j=y; (j+y<someImage.height) && (j<5); j++) {
				var value = someImage.data[(j+y)*someImage.width+ x+i ];
				display[i][j]=value;
			}
		}
		daldirty();
	}

	var showViewport = function(someImage, x, y) {
		var w = someImage.length;
		if (w <= 0)
			return;
		var h = someImage[0].length;

		for(var i=0; (i+x<w) && (i<5); i++) {
			for(var j=y; (j+y<h) && (j<5); j++) {
				var value = someImage[x+i][j+y];
				display[i][j]=value;
			}
		}
		daldirty();
	};

	function makeImage(imageAsString)
	{
		if (imageAsString.length)
		{
			var args = imageAsString.split(",");
			for(var i = 0; i < args.length; i++)
			{
				args[i] = parseInt(args[i]);
			}
			//console.log("makeImage " + args);
			var w = args.shift();
			var h = args.shift();

			var imageData = [];
			for(var col = 0; col < w; col++)
			{
				imageData[col] = [];
				for(var y = 0; y < h; y++)
				{
					imageData[col].push(args[y + (col*h)]);
				}
			}
			return imageData;
		}
		else
		{
			return [];
		}
	}

	var scrollImage = function(someImage, pausetime, w, h)
	{
		//console.log("scrollImage " + someImage + "w " + w + "h " + h);
		micro_device_ready = false;

		pausetime = pausetime || 80;
		imageToScroll = makeImage(w + "," + h + "," + someImage);
		imageToScrollW = w;
		imageToScrollH = h;

		imageScrollInterval = pausetime;
		imageScrollOffsetH = 0;


		handleScrollImage();
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
		showViewportStringSprite(myImage, mPP, 0);
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

	var getButton = function(id) {
		var butts = SIMIO.getButtons();

		if (id == 'A') {
			return (butts.A === true);
		}
		if (id == 'B') {
			return (butts.B === true);
		}
		return -1; // Signify error
	};

	var scrollString = function(str, delay)
	{
		delay = delay || 50;
		micro_device_ready = false;
		scrollSprite(new StringSprite(str), delay);
	};

	var setDirtyCallback= function(fn) {
		dirtyCallback = fn;
	};

	function handlePrintMessage(message, pausetime)
	{
		showLetter(message[0]);
		//console.log(message[0]);
		var rest = message.substr(1);
		if (rest.length) {
				setTimeout(
					function() { handlePrintMessage(rest, pausetime);},
					pausetime);
		} else {
			micro_device_ready = true;
		}
	}

	function handleScrollImage()
	{
		//console.log("handleScrollImage");
		clearDisplay();
		showViewport(imageToScroll, imageScrollOffsetH, 0);

		if (imageScrollOffsetH < imageToScrollW-DISPLAY_WIDTH+1)
		{
			//console.log("imageScrollOffsetH " + imageScrollOffsetH);
			imageScrollOffsetH++;
			setTimeout(handleScrollImage, imageScrollInterval);
		}
		else
		{
			micro_device_ready = true;
		}
	}

	function handleScrollSprite(sprite, delay)
	{
		if (scrollSpriteOffset < sprite.pixel_width())
		{
			sprite.render_string();
			sprite.pan_right();
			scrollSpriteOffset++;
			setTimeout(function(){
				handleScrollSprite(sprite, delay);
			}, delay);
		} 
		else 
		{
			micro_device_ready = true;
		}
	}

	var printMessage = function(message, pausetime) {
		printMessageStr = message;
		printMessageInterval = pausetime | 100;
		micro_device_ready = false;
		handlePrintMessage(message,printMessageInterval);
	};

	var scrollSprite = function(theSprite, delay)
	{
		delay = delay || 100;
		micro_device_ready = false;
		scrollSpriteOffset = 0;
		handleScrollSprite(theSprite, delay);
	};

	return {
		printMessage : printMessage,
		getButton : getButton,
		scrollImage : scrollImage,
		scrollString: scrollString,
		setDirtyCallback:setDirtyCallback,
		deviceReady:deviceReady,
//		Image:Image
	};
})();