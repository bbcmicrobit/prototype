#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance this license (or the alternative
# license below).
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# This file is also alternatively licensed under the terms of the GPL
# version 2. You may obtain a copy of the license at:
#
#     http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
from time import sleep

import sys
from PySide.QtCore import *
from PySide.QtGui import *

import sys
from PySide import QtGui

class MicrobugLoader(QtGui.QWidget):
    
    def __init__(self):
        super(MicrobugLoader, self).__init__()
        
        self.initUI()
        
    def initUI(self):      
        self.btn = QtGui.QPushButton('PROGRAM MICROBUG!', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
                
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Microbug Loader')
        self.show()

    def flashDevice(self, filename):
        os.system("c:\dfu-programmer-win-0.7.0\dfu-programmer.exe atmega32u4 flash " + filename)
        #os.system("dfu-programmer atmega32u4 flash " + filename)

    def eraseDevice(self):
        os.system("c:\dfu-programmer-win-0.7.0\dfu-programmer.exe atmega32u4 erase --force")
        #os.system("dfu-programmer atmega32u4 erase --force")

    def checkHexfileIsMicrobugFile(self): # This could be checked by looking for a magic string sequence
        return True
        
    def waitDeviceReady(self):
        # get devices plugged in to USB
        old_device_lines = []
        while True:
            while True:
                device_lines = os.popen('lsusb').readlines()
                if old_device_lines != device_lines:
                    old_device_lines = device_lines
                    break
                else:
                    sleep(1)
            #
            print "CHANGE IN USB DEVICES"
            #
            devices = []
            for device_line in device_lines:
                parts = device_line.split()
                _, busid, _, deviceid, _, usbid = parts[0:6]
                usbid = usbid.lower()
                devices.append(usbid)
            #       
            if "2341:8036" in devices:
                print "You need to plug in the device in 'program me' mode"
                print "You do this by plugging in an holding down button A"
            #
            if "03eb:2ff4" in devices:
                print "The device is now in program me mode, and will now"
                print "flash the device with your hex file"
                return


    def showDialog(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname:
            # self.waitDeviceReady()
            self.eraseDevice()
            self.flashDevice(fname)



def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MicrobugLoader()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
