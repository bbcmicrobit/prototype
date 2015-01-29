from py2exe.build_exe import py2exe
from distutils.core import setup
setup(
	data_files=[
                    "../../../add.png",
                    "../../../edit-copy.png",
                    "../../../editcut.png",
                    "../../../editpaste.png",
                    "../../../fileopen.png",
                    "../../../filesave.png",
                    "../../../redo.png",
                    "../../../run.png",
                    "../../../undo.png",
                    "../../../window-close.png"
	           ],
	windows=[{"script" : "../../../InteractiveTetherHost.py"}],
	options={
		"py2exe":
			{
				"dll_excludes":["MSVCP90.dll","HID.DLL","w9xpopen.exe"]
			}
	}
)
