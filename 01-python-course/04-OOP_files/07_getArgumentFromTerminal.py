#!/usr/bin/python3
"""
   Author        :     Amir W. Fathy
   Date          :     22 sep 2023
   Description   :     simple program get arguments from user in terminal and use it
"""


import sys

if len(sys.argv) < 2:
    print("Usage: 07_getArgumentFromTerminal.py numberOfOperation operation(+,-,x)")
    sys.exit(1)

l = []
arg1 = sys.argv[1]
arg2 = sys.argv[2]

for i in range(int(arg1)):
    try:
        l.append(int(input("Enter a number ")))
    except (ValueError):
        print("enter the number of operation you selected")
        sys.exit(1)


out = 0
product = 1

if arg2 == '+':
    for i in l:
        out += i
    print(out)
elif arg2 == '-':
    for i in l:
        out -= i
    print(out)
elif arg2 == 'x':
    for i in l:
        product = product*i
    print(product)
else:
    print("wrong operator")
