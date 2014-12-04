
all:
	make -f Makefile_arduino all

quiet:
	make -f Makefile_arduino all >build_arduino_log 2>&1

erase:
	dfu-programmer atmega32u4 erase --force

flash_device:
	dfu-programmer atmega32u4 flash build-leonardo/*.hex

clean:
	rm -rf build-leonardo
	rm -f *~