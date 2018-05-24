
# Building 

If you for some reason have decided to build Windows executable on your own:

The program is being built by [cx_Freeze](https://anthony-tuininga.github.io/cx_Freeze/):

`pip install cx_Freeze --upgrade`


Copy Python tcl86t.dll and tk86t.dll from the Python DLL folder into the root of your project (where the source is). Yes, I know that this is not very comfortable to build, but who even does that? 

Change `os.environ['TCL_LIBRARY']` paths to your TCL and TK lib paths.

Build with 

`python3 setup.py build`
