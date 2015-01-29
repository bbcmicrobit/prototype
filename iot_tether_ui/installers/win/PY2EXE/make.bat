rd /s /q dist
rd /s /q build
C:\Python27\python setup.py py2exe
copy ..\DFUPROG\dfu-programmer.exe dist\dfu-programmer.exe
copy ..\DFUPROG\libusb0.dll dist\libusb0.dll
copy ..\DFUPROG\libusb0.sys dist\libusb0.sys