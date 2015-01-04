while (getButton('B')) != PRESSED:
  if (getButton('A')) == PRESSED:
    scroll_string_image(StringImage('YOUR NAME'),50)
  else:
    scroll_string_image(StringImage('PRESS BUTTON A'),50)

