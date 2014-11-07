
while True:
    if getButton("A") == PRESSED:
        break
    delay(50)

scroll_sprite(StringSprite('HELLO WORLD'), 50)
delay(70)
scroll_sprite(StringSprite(":-) (:)"),50)
print "* * "
