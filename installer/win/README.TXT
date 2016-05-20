To build the Windows BBC Bug Loader
===================================

	Install Python for Windows (Version used: Python 2.7)

	Install PySide Binaries for Windows  (http://qt-project.org/wiki/PySide_Binaries_Windows)

	Install PY2EXE (http://www.py2exe.org) - ensure you install corresponding version, i.e. for Python 2.7

	Run /installer/win/PY2EXE/make.bat - further details can be found in /installer/win/PY2EXE/README.TXT

To build the Windows Microbug Installer 
=======================================

**Requires basic knowledge of Inno Installer and tinkering skills**

	Install Inno Installer (I used 2.1.0.20)

	Modify \installer\win\InnoSetupScript.iss to point to your clone of the BBCBug .git repo. There are five lines starting with C:\Users\Matthew\ that will need changing accordingly.

	Compile the modified InnoSetupScript to produce the installer.

LICENSE:
=======
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
