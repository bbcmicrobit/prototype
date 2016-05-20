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