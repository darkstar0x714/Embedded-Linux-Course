#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     22 sep 2023
   Description   :     simple email checker when computer is opening
"""

import pyautogui as gui
from time import sleep

gui.hotkey('win')
sleep(5)
gui.typewrite('thunder')
sleep(1)
gui.hotkey('enter')
sleep(5)
