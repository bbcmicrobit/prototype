#!/usr/bin/python


import time
from iotoy.deviceproxy import serial_io, DeviceProxy

io = serial_io("/dev/ttyACM0", 19200, debug=False)

mb = DeviceProxy(device=io)
mb.introspect_device()
io.dotimeout = False

mb.cleardisplay()
mb.eyeoff("A")
mb.eyeoff("B")

who = raw_input(">>> ")

while True:
    for i in range(3):
        mb.scrollstring(" Hello " + who +"!")
        mb.eyeon("A")
        time.sleep(1)
        mb.eyeon("B")
        time.sleep(1)
        
        mb.eyeoff("A")
        time.sleep(1)
        mb.eyeoff("B")
        time.sleep(1)

    time.sleep(300)
