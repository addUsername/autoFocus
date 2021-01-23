# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:44:03 2021

@author: SERGI
"""
from time import sleep
from win32api import MonitorFromPoint, GetCursorPos, keybd_event
from win32gui import GetForegroundWindow, ShowWindow, SetForegroundWindow
from win32con import KEYEVENTF_KEYUP

ALT = 0x09


def monitorWhereMousseIs():
    x, y = GetCursorPos()
    return str(MonitorFromPoint((x, y)))


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
    sleep(1)
