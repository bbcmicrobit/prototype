
all:
	make -f Makefile_arduino all

erase:
	sudo dfu-programmer atmega32u4 erase --force

flash_device:
	sudo dfu-programmer atmega32u4 flash build-leonardo/dal.hex

clean:
	rm -rf build-leonardo
	rm *~