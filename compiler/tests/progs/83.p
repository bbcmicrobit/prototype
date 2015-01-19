# Draw a pixel at 1,1
plot(1,1)
# This pauses the program briefly. The number is in thousandths of a second
pause(100)
while True:
  # Is the right button pressed
  # This is the condition for the if statement
  # We're looking at the state of a button
  # This is the name of the button. Button A is the left button, button B is the right button
  # This detects if the button is pressed or not pressed
  if (get_button('B')) == PRESSED:
    # Clear the screen
    clear_display()
  else:
    # Draw a pixel at 0,0
    # This means the left most column
    # top row
    plot(0,0)
