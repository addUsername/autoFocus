# autoFocus
Saves one click by set active the display's main window as mouse moves through different displays

## run this
- Create a new environment, install ``pywin32`` & ``pyinstaller==3.4`` [OPTIONAL] dependencies. and activate it.
- run ``python autofocus.py`` 

## pack it as .exe
- run ``pyinstaller autofocus.py --onefile --clean``
- the environment you just created is not needed anymore, you can safely remove it
- run ``/dist/autofocus.exe --help`` to see optional flags as ``--frecuency``,``--autostart``, ``--uninstall``
