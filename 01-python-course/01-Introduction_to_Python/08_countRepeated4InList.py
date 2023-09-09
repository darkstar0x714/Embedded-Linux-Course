#!/usr/bin/python3
""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     simple program print how many 4 in list entered by user 
"""

Input_list = input("enter list separated by space ")

Input_list = Input_list.split(" ")

print(f"number 4 is repeated {Input_list.count('4')} times in your list")
