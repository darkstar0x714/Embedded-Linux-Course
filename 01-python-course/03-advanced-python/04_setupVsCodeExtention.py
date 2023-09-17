#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     17 sep 2023
   Description   :     train to use pyautogui module to open vs code then setup an extension
"""
import pyautogui as gui
from time import sleep

gui.hotkey('win')
gui.typewrite('vscode')
sleep(1)
gui.hotkey('enter')
sleep(5)
gui.hotkey('ctrl', 'shift', 'x')
sleep(1)
gui.typewrite('clangd')
sleep(2)
gui.press('tab')
gui.press('down')
gui.press('tab')
gui.hotkey('enter')
sleep(2)
gui.hotkey('ctrl', 'shift', 'x')
sleep(1)
gui.typewrite('c++ TestMate')
sleep(2)
gui.press('tab')
gui.press('down')
gui.press('tab')
gui.hotkey('enter')
