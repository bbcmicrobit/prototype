while True:
  if (getButton('A')) == 1:
    show_image_offset(make_image(0x4,0x4,0x4,0xa,0x1f) ,0,0)
    pause(2000)
    clear_display()
  else:
    if (getButton('B')) == PRESSED:
      show_image_offset(make_image(0x1f,0x19,0x15,0x13,0x1f),0,0)
      pause(2000)
      clear_display()
