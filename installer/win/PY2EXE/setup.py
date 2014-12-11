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