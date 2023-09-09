#!/usr/bin/python3
""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     simple program to check is input is a vowel char or not 
"""

vowels = {'a', 'o', 'e', 'i', 'u'}

c = input("Enter the char please: ")

if c.lower() in vowels:
    print("you just entered a vowel char")
else:
    print("you just entered a not vowel char")
