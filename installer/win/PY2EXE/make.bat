REM
REM Copyright 2016 British Broadcasting Corporation and Contributors(1)
REM
REM (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
REM     not this header)
REM
REM Licensed under the Apache License, Version 2.0 (the "License"); you may
REM not use this file except in compliance this license (or the alternative
REM license below).
REM You may obtain a copy of the License at
REM
REM     http://www.apache.org/licenses/LICENSE-2.0
REM
REM This file is also alternatively licensed under the terms of the GPL
REM version 2. You may obtain a copy of the license at:
REM
REM     http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
REM
REM Unless required by applicable law or agreed to in writing, software
REM distributed under the License is distributed on an "AS IS" BASIS,
REM WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
REM See the License for the specific language governing permissions and
REM limitations under the License.
REM

rd /s /q dist
rd /s /q build
C:\Python27\python setup.py py2exe
copy ..\DFUPROG\dfu-programmer.exe dist\dfu-programmer.exe
copy ..\DFUPROG\libusb0.dll dist\libusb0.dll
copy ..\DFUPROG\libusb0.sys dist\libusb0.sys