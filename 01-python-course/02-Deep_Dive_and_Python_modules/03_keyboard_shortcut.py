#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     10 sep 2023
   Description   :     simple program make a shortcut to open python course
"""

import keyboard
import subprocess


def onTriggerCallBack():
    subprocess.run(["nautilus", "/home/darkstar0x714/courses/01Python"])


def listenForShortcut():
    shortcut = "e + l"

    keyboard.add_hotkey(shortcut, onTriggerCallBack)
    keyboard.wait()


listenForShortcut()
