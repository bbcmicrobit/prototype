while True:
  show_image_offset(make_image(0x0,0xe,0x11,0x0,0x0),0,0)
  set_eye('L',ON)
  set_eye('R',ON)
  pause(1000)
  set_eye('L',OFF)
  pause(100)
  set_eye('L',ON)
