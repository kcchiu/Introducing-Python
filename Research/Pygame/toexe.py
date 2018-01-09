# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 00:09:49 2018

@author: kcchi
"""

#import cx_Freeze
#import os
#from cx_Freeze import setup, Executable
#
#os.environ['TCL_LIBRARY'] = "C:\\Users\\kcchi\\Anaconda3\\tcl\\tcl8.6"
#os.environ['TK_LIBRARY'] = "C:\\Users\\kcchi\\Anaconda3\\tcl\\tcl8.6"
#
#build_exe_options = {'excludes': ['Tkinter']}
#
#executables = [cx_Freeze.Executable("highway.py")]
#
#cx_Freeze.setup(
#    name="Highway",
#    options={"build_exe": {"packages":["pygame"]}},
#    executables = executables,
#    version = "3.6"
#
#    )

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "highway",
        version = "0.1",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("highway.py", base=base)])