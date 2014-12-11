#!/usr/bin/python

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
        self.btn = QtGui.QPushButton('PROGRAM BUG!', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        self.btn.setGeometry(416, 295, 180, 30)

        pixmap = QtGui.QPixmap("Instructions1.png")

        palette = QPalette()
        palette.setBrush(QPalette.Background,QBrush(pixmap))

        self.setPalette(palette)
        self.setWindowTitle('BBC Bug Loader')
        self.setGeometry(300, 300, 723, 390)
        self.show()


    def flashDevice(self, filename):
        os.system('dfu-programmer atmega32u4 flash "' + filename + '"')

    def eraseDevice(self):
        os.system("dfu-programmer atmega32u4 erase --force")

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
            #self.waitDeviceReady()
            self.eraseDevice()
            self.flashDevice(fname)



def main():

    app = QtGui.QApplication(sys.argv)
    ex = MicrobugLoader()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
