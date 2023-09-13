#!/usr/bin/python3

""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     to print your name to the terminal with fancy way using pyfiglet module
"""
import pyfiglet

pyfiglet.FigletString("*")
result = pyfiglet.figlet_format("DarkStar0x714")

print(result)
