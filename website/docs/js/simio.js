var SIMIO = (function(){

	var canvas, context;

	var render = function(display, eyes) {

		// possibly the wrong way around...
		var displayWidth = display.length;
		var displayHeight = display[0].length;

		// DISPLAY
		//centre points nicely within canvas
		var xInc = canvas.width / (displayWidth + 1);
		var xOff = xInc / 2;
		var yInc = ((canvas.height/6)*5) / (displayHeight + 1);
		var yOff = canvas.height/6 + yInc / 2;
		var r = (xInc / 2.5);

		context.fillStyle = 'white';
		context.clearRect(0,0,canvas.width, canvas.height);

		context.fillStyle = 'red';

		for(var x = 0; x < displayWidth; x++){
			for(var y = 0; y < displayHeight; y++){
				if (display[x][y])
				{
					context.beginPath();
					context.arc(xOff + (x * xInc), yOff + (y * yInc), r, 0, 2 * Math.PI, false);
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
				context.arc(xOff + (i * (xInc*4)), yOff - yInc, r, 0, 2 * Math.PI, false);
				context.closePath();
				context.fill();
			}
			else
			{
				context.beginPath();
				context.arc(xOff + (i * (xInc*4)), yOff - yInc, r, 0, 2 * Math.PI, false);
				context.closePath();
				context.stroke();				
			}
		}
	};

	var init = function(divId) {
		canvas = document.createElement('canvas');
		canvas.width = document.getElementById(divId).clientWidth;
		canvas.height = canvas.width * (6/5); //extra row for eyes - TODO: makes assumption display is 5x5
		canvas.id = "simio";
		context = canvas.getContext('2d');

		document.getElementById(divId).appendChild(canvas);
	};

	return {
		init: init,
		render: render
	};
})();