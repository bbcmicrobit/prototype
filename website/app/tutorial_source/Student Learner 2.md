!Page:_tutorial_toolbox_1

# Beginner

-----------

## Turning LEDs on and off

!Page:_tutorial_toolbox_1

### Before you get started

Before you start coding there are three simple concepts you need to understand.

### How do I tell the difference betweens the LEDs

All of the LEDs look the same, but there is a simple way to tell them apart using X and Y co-ordinates.

Your X axis runs along the bottom of the grid, as shown on the diagram here.  The Y axis runs up the side.

The first row on X and and column on Y is 0.  The next is 1 and so on.

**TODO: Images live here**
![Melon Cat](static/microbug/tutorial_assets/melon-cat.jpg)

So if we want to identify this LED here *(Diagram 2)* we count 3 rows along the X axis and 5 up the Y axis.  (Meaning this LEDs name is X2 Y4).

Each of the LED state blocks has a space where you can enter the X and Y numbers you need.

### How does an LED know to turn on or off?

Binary code consists entirely of 1s and 0s.  If you want a light to come on, you'll need to enter 1.  If you want it to be off you need to enter 0.

OFF = 0
ON = 1

!Page:_tutorial_toolbox_1
### What does the code actually look like?

The technical name for the code you will be working with is JavaScript.  Which looks like this:

    <!DOCTTYPE html>
    <html>
    <body>
    
    <p id="demo"></p>
    
    <script>
    document.getElementById('demo').innerHTML = '123e5';
    </script>

But to help make things a bit easier we've created visual building blocks that you can arrange in the workspace.  By simply dragging and dropping different blocks and attacking them to each other in sequence, you can assemble your code a lot more quickly.

They'll give exactly the same instructions to Micro Bug, you just need to change the numbes on each block to get the results you want.

And when you've finished a creation, you can see what it looks like as JavaScript by pressing the JavaScript button at the top of the workspace.

----

### *Task 1:* Turning the LED on

Let's get an LED on the Micro Bug to light up.  This is also called 'setting the LED state'.

* **a** To do this go to the LED menu and select a *set LED state block*.

**TODO: Image lives here **

* **b** Because both X and Y are set to 0, this command will go straight to the LED at the bottom left of your grid.

* **c** By setting the state to 1 we are turning it ON (Remember 0 = OFF and 1 = On)

* **d** If you click the play button now you should see that the LED on the bottom left lights up.

** TODO: Image lives here **

* **e** If you have time, try changing one of the X or Y numbers to make a different LED light up.  If you do, change it back to 0 again before starting task 2.

!Page:_tutorial_toolbox_1

### *Task 2:* Turning the LED off again

To turn the LED OFF again we'll need to add an instruction.

* **a** First of all we need a *pause for time (ms)* block.  Select one from the Basic menu, then place this underneath the *set LED state* block you already have.

* **b** Pause blocks count everything in milliseconds to give you lots of control for sophisticated coding later on.  For now, just remember 1000ms = 1 second.

* **c** To change your LED state to OFF we'll need to select another *set LED state* block and drag this underneath the *pause for time (ms)* block.

* **d** We're instructing the light we just turned on, so the X and Y numbers should be exactly the same as they are in the first block.  The only thing we need to change is the state.  OFF=0 so set that number *to 0*, as we've done below.

** TODO: Image lives here **

* **e** If you click the play button now you should see that the LED on the bottom left:
    * Lights up
    * Pauses for 1 second
    * And then turns off

** TODO: Image lives here **

Done it?  Great!  Let's try turning multiple LEDs on at the same time.

!Page:_tutorial_toolbox_1

### *Task3:* Turning the LED off again

* **a** If we want to turn on lots of LEDs simultaneously we will need lots of *LED state blocks*

* **b** Using exactly the same kind of instructions as task 2 we can create a leter T.

* **c** To do this we need to turn on a row of 4 LEDs at the top, and a column of 4 LEDs in the middle.  So we'll need 8 *LED state* blocks.

* **d** Using the X and Y counting system you learned earlier, identify each LED that you need and set the state to 1 (just like we've done below)

* **e** You'll need a *pause for time (ms)* block at the end too.

** TODO: Image lives here **


!Page:_tutorial_toolbox_1

### *Task 4*: Create your own initials

If your first initial starts with a T then this will be a little easy, so pick another letter.

* **a** First, use a pencil to colour in the LEDs on a Micro Bug worksheet, to decide the best way to show your initial.  For instance an L will be very like a T, except you need your X row at the bottom and your Y column on the left.

* **b** Once you are ready select the appropriate number of *LED state* blocks, then enter the X and Y numbers and set all of their states to 1 (ON).

* **c** Now add a *pause for time(ms)* block and see how it looks by pressing PLAY

* **d** Done?  Then try adding your second initial to the code too.

----

### *TOP TIP:* Try changing the speed

You can adjust the speed that your instructions play as they light up using the SPEED SLIDER.  This will show the program running through your sequence of instructions one at a time, to help you check that everything is working the way you want it to.
