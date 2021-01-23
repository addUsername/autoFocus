# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:44:03 2021

When this script becomes .exe thx to pyinstaller, may be detected by the system
as TROJAN, I've downgraded pyinstaller to 3.4.
Making this .exe as --one-file may be catched as TROJAN too.
This needs a self signed certificated
https://stackoverflow.com/questions/43777106/program-made-with-pyinstaller-now-seen-as-a-trojan-horse-by-avg
@author: SERGI
"""
from time import sleep
from win32api import MonitorFromPoint, GetCursorPos, keybd_event
from win32gui import GetForegroundWindow, ShowWindow, SetForegroundWindow
from win32con import KEYEVENTF_KEYUP
from argparse import ArgumentParser

ALT = 0x09
F = 1


def monitorWhereMousseIs():
    return str(MonitorFromPoint(GetCursorPos()))


def getActiveWindow():
    return GetForegroundWindow()


def showMainWindowFromMonitor(window):
    ShowWindow(window, 5)
    pressAlt()
    SetForegroundWindow(window)


# win32api.SetForegroundWindow() needs this.. idk
def pressAlt():
    keybd_event(ALT, 0, 0, 0)
    sleep(.05)
    keybd_event(ALT, 0, KEYEVENTF_KEYUP, 0)


ap = ArgumentParser()
ap.add_argument("-f", "--frecuency", required=False,
                help="frecuency each iteration occurs (in s)")

ap.add_argument("-u", "--uninstall", required=False,
                help="delete .bat file from auto-start folder")

ap.add_argument("-u", "--autostart", required=False,
                help="set autoFocus.bat in auto-start folder")

args = vars(ap.parse_args())

if args["frecuency"] is not None:
    F = float(args["frecuency"])


current_monitor = monitorWhereMousseIs()
monitors = {}
monitors[monitorWhereMousseIs()] = getActiveWindow()

while(True):
    if(monitorWhereMousseIs() != current_monitor):
        current_monitor = monitorWhereMousseIs()

        if current_monitor in monitors:
            showMainWindowFromMonitor(monitors[monitorWhereMousseIs()])
    else:
        monitors[monitorWhereMousseIs()] = getActiveWindow()
    print(monitors)
    sleep(F)
