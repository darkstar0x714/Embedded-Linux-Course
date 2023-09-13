#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     10 sep 2023
   Description   :     simple program to print the max number from given list
"""

x = input("enter list elements separated by ',' ")

list1 = list(map(int, x.split(",")))

print(f"the largest element in the list is {max(list1)}")
