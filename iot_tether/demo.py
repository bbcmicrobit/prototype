#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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
