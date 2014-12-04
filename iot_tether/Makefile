
all:
	make -f Makefile_arduino all

erase:
	dfu-programmer atmega32u4 erase --force

flash_device:
	dfu-programmer atmega32u4 flash build-leonardo/*.hex

clean:
	rm -rf build-leonardo
	rm *~