# autoFocus
Saves one click by set active the display's main window as mouse moves through different displays. Windows only

## click & run
- open ``autofocus.exe``
- run on start: edit and copy ``autorun.bat`` to ``C:\Users\[USER]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\autorun.bat`` **rename if needed**

## run this
- Create a new environment, install ``pywin32`` & ``pyinstaller==3.4`` [OPTIONAL] dependencies. and activate it.
- run ``python autofocus.py [number]``
- run ``python setup.py --help`` to see optional flags as ``--frecuency``,``--autostart``, ``--uninstall``

## pack it as .exe
- run ``pyinstaller autofocus.py --onefile --clean``
- the environment you just created is not needed anymore, you can safely remove it
- run ``/dist/autofocus.exe`` or with ``/d`` to hide terminal window
