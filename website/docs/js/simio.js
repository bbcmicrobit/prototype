var SIMIO = (function(){

	var canvas, context;

	var render = function(display) {

		// possibly the wrong way around...
		var displayWidth = display.length;
		var displayHeight = display[0].length;

		//centre points nicely within canvas
		var xInc = canvas.width / (displayWidth + 1);
		var xOff = xInc / 2;
		var yInc = canvas.height / (displayHeight + 1);
		var yOff = yInc / 2;
		var r = (xInc / 2.5);

		context.fillStyle = 'white';
		context.clearRect(0,0,canvas.width, canvas.height);

		context.fillStyle = 'green';

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
	};

	var init = function(divId) {
		canvas = document.createElement('canvas');
		canvas.width = document.getElementById(divId).clientWidth;
		canvas.height = canvas.width;
		canvas.id = "simio";
		context = canvas.getContext('2d');

		document.getElementById(divId).appendChild(canvas);
		DALJS.setDirtyCallback(render);
	};

	return {
		init: init,
		render: render
	};
})();