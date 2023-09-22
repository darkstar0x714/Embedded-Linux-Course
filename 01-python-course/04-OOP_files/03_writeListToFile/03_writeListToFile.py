#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     20 sep 2023
   Description   :     simple program to write list to txt file
"""
l = []

for i in range(1, 51):
    l.append(str(i))

try:
    with open("03_list.txt", "w") as f:
        f.write("\n".join(l))

except PermissionError:
    print("you don't have permission to open")
