import sys
import os
from cx_Freeze import setup, Executable

# This is hidden until we display progress inside GUI, for now we need a console window

# base = None
# if sys.platform == 'win32':
    # base = 'Win32GUI'

base = "Console"    
    
executables = [
    Executable('grant.py', base=base)
]

buildOptions = dict(include_files = ["tcl86t.dll", "tk86t.dll"], optimize=1)

# Change those to your paths when building
os.environ['TCL_LIBRARY'] = r'C:\Users\root\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\root\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

setup(name='PGrant',
      version='0.4',
      description='Valve promo distribution tool',
      executables=executables,
      options = dict(build_exe = buildOptions)
      )