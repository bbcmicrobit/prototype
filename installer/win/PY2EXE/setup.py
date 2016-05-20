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

from py2exe.build_exe import py2exe
from distutils.core import setup
setup(
	data_files=["../DFUPROG/Instructions1.png"],
	windows=[{"script":"../DFUPROG/BBCBugLoader.py"}],
	options={
		"py2exe":
			{
				"dll_excludes":["MSVCP90.dll","HID.DLL","w9xpopen.exe"]
			}
	}
)