#!/usr/bin/python


import feedparser
import time
from iotoy.deviceproxy import serial_io, DeviceProxy


io = serial_io("/dev/ttyACM1", 19200, debug=False)

mb = DeviceProxy(device=io)
mb.introspect_device()
io.dotimeout = False

mb.cleardisplay()

source = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
for entry in source["entries"]:
    item = str(entry["title"])
    item = item.replace("VIDEO: ","")
    item = item.replace("In pictures: ","")
    item = " "+ item + "----"
    print item
    mb.scrollstring(item.upper())
