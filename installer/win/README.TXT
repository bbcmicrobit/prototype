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