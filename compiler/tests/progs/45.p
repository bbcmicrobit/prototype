i = None


while (getButton('B')) != 1:
  if (getButton('A')) == 1:
    scroll_string_image(StringImage('YOUR NAME'),50)
  else:
    scroll_string_image(StringImage('PRESS BUTTON A'),50)
for i in range(6):
  scroll_string_image(StringImage(i),50)
