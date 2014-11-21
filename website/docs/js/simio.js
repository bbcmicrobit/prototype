var SIMIO = (function(){

	var canvas, context, imageObj;

	var ledColumns = [0.298, 0.368, 0.44, 0.508, 0.58];
	var ledRows = [0.564,0.636,0.708,0.776,0.846];
	var ledEyes = [[0.244, 0.196],[0.624, 0.186]];

	var buttons = [[0.108, 0.274][0.762, 0.27]];
	var buttonState = [false, false];

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

	var buttonHitBox = [new BBOX([0.066, 0.232],[0.164, 0.328]),new BBOX([0.704, 0.232],[0.81, 0.332])];

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

	var six = 6;
	var five = 5;

	var render = function(display, eyes) {

		context.fillStyle = 'grey';
		context.fillRect(0,0,canvas.width, canvas.height);
//		context.clearRect(0,0,canvas.width, canvas.height);
		
		context.save();
		var scaleFactor = Math.min(canvas.height, canvas.width) / Math.max(imageObj.height, imageObj.width);
		context.scale(scaleFactor, scaleFactor);
        context.drawImage(imageObj, 0, 0);
		context.restore();		

		// Might get called without display data, in which case get out here.
		if (!(display && eyes))
			return;
		else
		{
			// possibly the wrong way around...
			var displayWidth = display.length;
			var displayHeight = display[0].length;

			// DISPLAY
			//centre points nicely within canvas
			var xInc = canvas.width / (displayWidth + 1);
			var xOff = xInc / 2;
			var yInc = ((canvas.height/six)*five) / (displayHeight + 1);
			var yOff = canvas.height/six + yInc / 2;
			var r = canvas.width / 40;//(xInc / 2.5);

			context.fillStyle = 'red';

			for(var x = 0; x < displayWidth; x++){
				for(var y = 0; y < displayHeight; y++){
					if (display[x][y])
					{
						context.beginPath();
						context.arc(ledColumns[x] * canvas.width, ledRows[y] * canvas.height, r, 0, 2 * Math.PI, false);
						context.closePath();
						context.fill();
					}
				}
			}

			// EYES
			context.fillStyle = 'orange';
			context.strokeStyle = 'orange';
			for(var i = 0; i < eyes.length; i++)
			{
				if (eyes[i])
				{
					context.beginPath();
					context.arc(ledEyes[i][0] * canvas.width, ledEyes[i][1] * canvas.height, r, 0, 2 * Math.PI, false);
					context.closePath();
					context.fill();
				}
			}
		}
	};



	var init = function(divId) {
		canvas = document.createElement('canvas');
		canvas.width = document.getElementById(divId).clientWidth;
		canvas.height = canvas.width;
		canvas.id = "simio";
		context = canvas.getContext('2d');

		function getCursorPosition(e) {
			var x;
			var y;
			if (e.pageX != undefined && e.pageY != undefined) {
				x = e.pageX;
				y = e.pageY;
			}
			else {
				x = e.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
				y = e.clientY + document.body.scrollTop + document.documentElement.scrollTop;
			}

			x -= canvas.offsetLeft;
			y -= canvas.offsetTop;
			return [x,y];
		}

		canvas.addEventListener('mousedown', function(e) {
			var pos = getCursorPosition(e);
			var clickedX = pos[0];
			var clickedY = pos[1];
			var nx = clickedX / canvas.width, ny = clickedY / canvas.height;
			var whichButtonPressed = checkButtonsForMouseClick(nx, ny);
			console.log("canvas clicked at " + nx + ", " + ny + " resulting in button " + whichButtonPressed);

			if (whichButtonPressed !== -1)
			{
				buttonState[whichButtonPressed] = true; 
			}
		}, false);		

		canvas.addEventListener('mouseup', function(e) {
			buttonState = [false, false];//MRBTODO what if you have TWO MICE! (or something)
		}, false);


		imageObj = new Image();
		imageObj.addEventListener('load',function(){
			SIMIO.render();
		});
		imageObj.src = 'media/IMG_8829.png';

		document.getElementById(divId).appendChild(canvas);
	};

	return {
		init: init,
		render: render,
		getButtons: function () {return {A:buttonState[0],B:buttonState[1]};},
	};
})();