# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 22:02:39 2021

@author: SERGI
"""
from argparse import ArgumentParser
from win32file import CopyFile, DeleteFile
from getpass import getuser
from os import getcwd

F = 1
OUTPUT = False


def add_to_startup():
    startup_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\autorun.bat' % getuser()
    bat_path = getcwd()+"\\autorun.bat"

    f = open(bat_path, "w")
    f.write("start " + getcwd() + " autofocus.exe " + str(F) + " " + str(OUTPUT))
    f.close()
    CopyFile(bat_path, startup_path, 0)


def uninstall():
    DeleteFile(
        r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\autorun.bat' % getuser())


ap = ArgumentParser()
ap.add_argument("-f", "--frecuency", required=False,
                help="frecuency each iteration occurs (in s)")

ap.add_argument("-u", "--uninstall", required=False,
                help="delete .bat file from auto-start folder,, NEEDS ADMIN")

ap.add_argument("-a", "--autostart", required=False,
                help="set autoFocus.bat in auto-start folder, NEEDS ADMIN")

ap.add_argument("-o", "--output", required=False,
                help="enable print()")

args = vars(ap.parse_args())

if args["frecuency"] is not None:
    F = float(args["frecuency"])

if args["output"] is not None:
    OUTPUT = True

if args["autostart"] is not None:
    if(args["autostart"].lower() == "true"):
        add_to_startup()
        print("finish, press a key to continue..")
        input()
        exit(0)

if args["uninstall"] is not None:
    if(args["uninstall"].lower() == "true"):
        uninstall()
        print("finish, press a key to continue..")
        input()
        exit(0)