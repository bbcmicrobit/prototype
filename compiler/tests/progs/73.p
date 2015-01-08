bear_name = None
happy_bear = None
sad_bear = None
oh_bear = None
confused_bear = None

bear_name = 0
happy_bear = make_image(0xe,0x11,0x4,0xa,0xa)
sad_bear = make_image(0x11,0xe,0x0,0x4,0x1b)
oh_bear = make_image(0xe,0xa,0x4,0x1b,0xa)
confused_bear = make_image(0x1f,0x0,0x4,0xa,0x1b)
show_image_offset(happy_bear,0,0)

while True:
    if (get_button('a')==True and get_button('b')==True):
        show_image_offset(happy_bear,0,0)
    if (get_button('a')==False and get_button('b')==True):
        show_image_offset(oh_bear,0,0)
    if (get_button('a')==True and get_button('b')==False):
        show_image_offset(confused_bear,0,0)
    if (get_button('a')==False and get_button('b')==False):
        show_image_offset(sad_bear,0,0)
    pause(400)
