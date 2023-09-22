#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     20 sep 2023
   Description   :     simple program to count number of words in file 
"""

try:
    with open("01_numberOfLines/01_lines.txt", "r") as file:
        r = file.read().split()
    print(f"number of lines is  = {len(r)}")

except FileNotFoundError:
    print("file not exist")
except PermissionError:
    print("you don't have permission to open")
