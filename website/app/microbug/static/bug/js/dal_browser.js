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

	var timeoutHandle;

	var paused = false;

	function deviceReady() {
		return micro_device_ready;
	}

	function SpriteImage(imageData)
	{
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
			dirtyCallback(display);
	}

	var clear_display = function()
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

	var show_letter = function(c) {

		if (typeof(c) === "string")
		{
			c = c.charCodeAt(0);
		}

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

		daldirty();
	};

	var showViewportStringImage = function(someImage, x, y)
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

	var show_image_offset = function(someImage, x, y) {
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

	var scroll_image = function(someImage, pausetime, w, h)
	{
		//console.log("scroll_image " + someImage + "w " + w + "h " + h);
		micro_device_ready = false;

		pausetime = pausetime || 80;
		imageToScroll = makeImage(w + "," + h + "," + someImage);
		imageToScrollW = w;
		imageToScrollH = h;

		imageScrollInterval = pausetime;
		imageScrollOffsetH = 0;


		handleScrollImage();
	};

	// function StringImage(str) {
	// 	this.mPixelPos = 0;
	// 	this.mPixelData = []; // was [50] Sufficient to hold two characters.
	// 	this.mString = "";
	// 	this.mStrlen = 0;

	// 	if(str !== undefined)
	// 		this.setString(str);
	// }

	function StringImage(pp, pd, string, strlen)
	{
		this.mPixelPos = pp;
		this.mPixelData = pd;
		this.mString = string;
		this.mStrlen = strlen;

		if(this.mString !== undefined)
			this.setString(this.mString);
	}

	StringImage.prototype.setString = function(str)
	{
		this.mString = str;
		this.mPixelPos = 0;
		for(var i=0; i++; i<50) {
			this.mPixelData[i] = 0;
		}
		this.mStrlen = this.mString.length;
	};

	StringImage.prototype.update_display = function()
	{
		var myImage = new SpriteImage();
		var mPP = this.mPixelPos%5;
		myImage.width = 10;
		myImage.height = 5;
		myImage.data = this.mPixelData;
		showViewportStringImage(myImage, mPP, 0);
	};

	StringImage.prototype.render_string = function() {
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

	StringImage.prototype.pan_right = function() {
		this.mPixelPos += 1;
		if (this.mPixelPos>=this.pixel_width()) {
			this.mPixelPos = 0;
		}
	};

	StringImage.prototype.pixel_width = function() {
		return this.mStrlen * 5;
	}; 

	var get_button = function(id) {
		var butts = SIMIO.getButtons();

		if ((id == 'A') || (id == 'a') || (id == 'L') || (id == 'l')) {
			return (butts.A === true);
		}
		if ((id == 'B') || (id == 'b') || (id == 'R') || (id == 'r')) {
			return (butts.B === true);
		}
		return false; // Signify error
	};

//	function StringImage(pp, pd, string, strlen)

	// 	this.mPixelPos = 0;
	// 	this.mPixelData = []; // was [50] Sufficient to hold two characters.
	// 	this.mString = "";
	// 	this.mStrlen = 0;



	var scroll_string = function(str, delay)
	{
		delay = delay || 50;
		micro_device_ready = false;
		scroll_string_image(new StringImage(0, [], str, 0), delay);
	};

	var setDirtyCallback= function(fn) {
		dirtyCallback = fn;
	};

	function handlePrintMessage(message, pausetime)
	{		
		timeoutHandle = undefined;

		show_letter(message[0]);
		//console.log(message[0]);
		var rest = message.substr(1);
		if (rest.length) {
				timeoutHandle = setTimeout(
					function() { handlePrintMessage(rest, pausetime);},
					pausetime);
		} else {
			micro_device_ready = true;
		}
	}

	function pause(pausetime)
	{
		timeoutHandle = undefined;
		micro_device_ready = false;
		timeoutHandle = setTimeout(function() {micro_device_ready = true;}, pausetime);
	}

	function handleScrollImage()
	{
		timeoutHandle = undefined;
		//console.log("handleScrollImage");
		clear_display();
		show_image_offset(imageToScroll, imageScrollOffsetH, 0);

		if (imageScrollOffsetH < imageToScrollW-DISPLAY_WIDTH+1)
		{
			//console.log("imageScrollOffsetH " + imageScrollOffsetH);
			imageScrollOffsetH++;
			timeoutHandle = setTimeout(handleScrollImage, imageScrollInterval);
		}
		else
		{
			micro_device_ready = true;
		}
	}

	function handleScrollSprite(sprite, delay)
	{
		timeoutHandle = undefined;

		if (scrollSpriteOffset < sprite.pixel_width())
		{
			sprite.render_string();
			sprite.pan_right();
			scrollSpriteOffset++;
			timeoutHandle = setTimeout(function(){
				handleScrollSprite(sprite, delay);
			}, delay);
		} 
		else 
		{
			micro_device_ready = true;
		}
	}

	var print_message = function(message, pausetime) {
		printMessageStr = message;
		printMessageInterval = pausetime | 100;
		micro_device_ready = false;
		handlePrintMessage(message,printMessageInterval);
	};

	var scroll_string_image = function(theSprite, delay)
	{
//	function StringImage(pp, pd, string, strlen)
		var newSprite = new StringImage(theSprite.mPixelPos, theSprite.mPixelData, theSprite.mString, theSprite.mStrlen);
		delay = delay || 100;
		micro_device_ready = false;
		scrollSpriteOffset = 0;
		handleScrollSprite(newSprite, delay);
	};

	var halt = function()
	{
		// Stop execution of any timeout functions
		if (timeoutHandle !== undefined)
		{
			console.log("daljs clearing timeout");
			clearTimeout(timeoutHandle);
			timeoutHandle = undefined;
			micro_device_ready = true;			
		}
	}

	// var pause = function(_paused)
	// {
	// 	paused = _paused;
	// }

	return {
		print_message : print_message,
		get_button : get_button,
		scroll_image : scroll_image,
		scroll_string: scroll_string,
		scroll_string_image: scroll_string_image,
		pause : pause,
		setDirtyCallback:setDirtyCallback,
		deviceReady:deviceReady,
//		pause: pause,
		halt: halt
	};
})();