#!/usr/bin/python3
""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     simple calculator to performe simple operations (+,-,*,/)
"""

from termcolor import colored


x = int(input("Enter first number = "))
c = input("Enter operation +,-,/,* or E to exit is ")
y = int(input("Enter second number = "))


if c == '+':
    print(f"{x} + {y} = ", colored(x+y, 'green'))
elif c == '-':
    print(f"{x} - {y} = ", colored(x-y, 'green'))
elif c == '*':
    print(f"{x} * {y} = ", colored(x*y, 'green'))
elif c == '/':
    print(f"{x} / {y} = ", colored(x/y, 'green'))
else:
    print(colored("invalid operation", "red"))
