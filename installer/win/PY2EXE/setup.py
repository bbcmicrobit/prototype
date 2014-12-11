from py2exe.build_exe import py2exe
from distutils.core import setup
setup(
	data_files=["../DFUPROG/microbug-small.png"],
	windows=[{"script":"../DFUPROG/MicrobugLoader.py"}],
	options={
		"py2exe":
			{
				"dll_excludes":["MSVCP90.dll","HID.DLL","w9xpopen.exe"]
			}
	}
)