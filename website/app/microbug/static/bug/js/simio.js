var SIMIO = (function(){

	var canvas, context, imageObj, flareObj, flareObj2;

	var ledColumns = [0.305, 0.38, 0.455, 0.525, 0.6];
	var ledRows = [0.55,0.625,0.685,0.755,0.83];
	var ledEyes = [[0.265, 0.205],[0.635, 0.2]];

	var buttonState = [false, false];

	var eyeState = [false, false];




	//a, b, l, r and cursor left right can be used for button inputs
	window.addEventListener("keydown", function(e){
		if (e.keyCode == 65 || e.keyCode == 76 || e.keyCode == 37) //A,L,<-
		{
			buttonState[0] = true;
		}
		if (e.keyCode == 66 || e.keyCode == 82 || e.keyCode == 39) //B,R,->
		{
			buttonState[1] = true;
		}
	});
	window.addEventListener("keyup", function(e){
		if (e.keyCode == 65 || e.keyCode == 76 || e.keyCode == 37)
		{
			buttonState[0] = false;
		}
		if (e.keyCode == 66 || e.keyCode == 82 || e.keyCode == 39)
		{
			buttonState[1] = false;
		}
	});

	function BBOX(tl,br)
	{
		this.tl = tl;
		this.br = br;
	}

	BBOX.prototype.check = function(x, y)
	{
		if (x >= this.tl[0] && x <= this.br[0] && y >= this.tl[1] && y <= this.br[1])
			return true;
		else
			return false;
	}


	var buttonHitBox = [new BBOX([0.05, 0.26],[0.165, 0.36]),new BBOX([0.74, 0.25],[0.86, 0.365])];

	function checkButtonsForMouseClick(x, y)
	{
		for(var i = 0; i < buttonHitBox.length; i++)
		{
			if (buttonHitBox[i].check(x,y))
				return i;
		}
		return -1;
	}

	function Button()
	{
		this.x = 0;
		this.y = 0;
		this.r = 0;
		this.pressed = false;
	}

	var buttons = [new Button(), new Button()];

	var ledScale = 1;

	function drawLed(img, x, y)
	{
		ledScale = (canvas.width / flareObj.width) * 0.15;

		context.save();
		context.translate(x - (img.width * ledScale)/2, y - (img.height * ledScale)/2);
		context.scale(ledScale, ledScale);
		context.drawImage(img, 0, 0);
		context.restore();
	}

	var render = function(display, eyes) {

		// Draw bug	
		context.globalCompositeOperation = "source-over";
		context.fillStyle = 'white';
		context.fillRect(0,0,canvas.width, canvas.height);
	
		context.save();
		var scaleFactor = Math.min(canvas.height, canvas.width) / Math.max(imageObj.height, imageObj.width);
		context.scale(scaleFactor, scaleFactor);
        context.drawImage(imageObj, 0, 0);
		context.restore();		

		// Draw leds
		if (!display)
			return;

		//resolve numbers to booleans, JIC
		if (eyes)
		{
			eyeState[0] = (eyes[0] ? true : false);
			eyeState[1] = (eyes[1] ? true : false); 
		}
		
		context.globalCompositeOperation = "lighter";

		var displayWidth = display.length;
		var displayHeight = display[0].length;

		for(var x = 0; x < displayWidth; x++){
			for(var y = 0; y < displayHeight; y++){
				if (display[x][y])
				{
					drawLed(flareObj, ledColumns[x] * canvas.width, ledRows[y] * canvas.height);
				}
			}
		}

		// EYES
		for(var i = 0; i < eyeState.length; i++)
		{
			if (eyeState[i])
			{
				drawLed(flareObj2, ledEyes[i][0] * canvas.width, ledEyes[i][1] * canvas.height);
			}
		}
	};

	var init = function(divId) {
		canvas = document.createElement('canvas');
		canvas.width = document.getElementById(divId).clientWidth;
		canvas.height = canvas.width;
		canvas.id = "simio";
		context = canvas.getContext('2d');

		imageObj = new Image();
		imageObj.addEventListener('load',function(){
			SIMIO.render();
		});
//		imageObj.src = '/static/bug/media/IMG_9125.png';
		imageObj.src = '/static/bug/media/Bug.jpg';

		flareObj = new Image();
		flareObj.src = '/static/bug/media/redledwithalpha_sm.png';

		flareObj2 = new Image();
		flareObj2.src = '/static/bug/media/orangeledwithalpha_sm.png';

		document.getElementById(divId).appendChild(canvas);
		var button = document.createElement('button');
		button.style.position = 'absolute';
		button.style.width = '200px';
		button.style.height = '200px';
		button.style.marginLeft = '-200px';
		button.style.background = 'none';
		button.style.border = 'none';
		button.style.outline = 'none';
		button.style.padding = '0px';
		document.getElementById(divId).appendChild(button);

		button.onmousedown=function(e) {
			var pos = [e.offsetX / canvas.width, e.offsetY / canvas.height];
			var whichButtonPressed = checkButtonsForMouseClick(pos[0], pos[1]);
			console.log("canvas clicked at " + pos[0] + ", " + pos[1] + " resulting in button " + whichButtonPressed);

			if (whichButtonPressed !== -1)
			{
				buttonState[whichButtonPressed] = true; 
			}
		};
		button.onmouseup=function(e) {
			buttonState = [false, false];
		};
		button.onmouseleave=function(e) {
			buttonState = [false,false];
		}
	};

	return {
		init: init,
		render: render,
		getButtons: function () {return {A:buttonState[0],B:buttonState[1]};},
	};
})();