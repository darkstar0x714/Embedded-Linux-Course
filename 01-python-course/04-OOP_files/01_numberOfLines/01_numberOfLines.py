#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     20 sep 2023
   Description   :     simple program to count number of lines in file 
"""


try:
    with open("01_lines.txt", "r") as file:
        r = file.readlines()
    print(f"number of lines is  = {len(r)}")

except FileNotFoundError:
    print("file not exist")
except PermissionError:
    print("you don't have permission to open")
