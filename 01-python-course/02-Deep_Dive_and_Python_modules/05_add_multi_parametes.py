#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     12 sep 2023
   Description   :     program to print the sum of input to function using multi argument style
"""


def sum(*input):
    sum = 0
    inputLen = len(input)
    for i in range(inputLen):
        sum += input[i]
    print(f"the sum of the functions is = {sum}")


sum(1, 2, 3, 6, 4)
