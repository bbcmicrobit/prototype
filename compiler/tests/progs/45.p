i = None


while (get_button('B')) != 1:
  if (get_button('A')) == 1:
    scroll_string_image(StringImage('YOUR NAME'),50)
  else:
    scroll_string_image(StringImage('PRESS BUTTON A'),50)
for i in range(6):
  scroll_string_image(StringImage(i),50)
