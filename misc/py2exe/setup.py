# setup.py
# A setup.py for py2exe for building a Pigeon Feather exe
from distutils.core import setup
import py2exe

setup(
    windows=['pigeonfeather.py'],
	options={
		"py2exe":{
			"optimize": 2,
			"bundle_files": 1,
			"compressed": True,
			"includes":["sip"],
			"excludes":['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email',
				'pywin.debugger', 'pywin.debugger.dbgcon', 'pywin.dialogs',
                'tcl', 'Tkconstants', 'Tkinter'],
			"packages":["lxml", "gzip"]
                }
            }
    )
