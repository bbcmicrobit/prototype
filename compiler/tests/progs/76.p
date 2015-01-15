scores = 0
facetoshow = make_image(0x0,0x0,0x0,0x0,0x0)
farts = make_image(0x1f,0x11,0x0,0xa,0xa)
FLC = make_image(0x11,0x1f,0x0,0xa,0xa)
facetoshow = farts
show_image_offset(facetoshow,0,0)
for count in range(6):
  pause(400)
  if get_button('A'):
    scores = scores + 1
  elif get_button('B'):
    scores = scores - 1
facetoshow = FLC
show_image_offset(facetoshow,0,0)
for count2 in range(6):
  pause(400)
  if get_button('A'):
    scores = scores - 1
  elif get_button('B'):
    scores = scores + 1
facetoshow = FLC
show_image_offset(facetoshow,0,0)

for count3 in range(5):
  pause(400)
  if get_button('A'):
    scores = scores - 1
  elif get_button('B'):
    scores = scores + 1
facetoshow = farts

show_image_offset(facetoshow,0,0)
for count4 in range(4):
  pause(300)
  if get_button('A'):
    scores = scores + 1
  elif get_button('B'):
    scores = scores - 1
clear_display()
scroll_string_image(StringImage(scores),100)
if scores > 5:
  facetoshow = farts
else:
  facetoshow = FLC
show_image_offset(facetoshow,0,0)
