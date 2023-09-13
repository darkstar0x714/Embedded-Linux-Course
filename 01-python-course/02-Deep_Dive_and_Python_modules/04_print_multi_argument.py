#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     12 sep 2023
   Description   :     simple program to print the function input 
                       list and dic content without know len of
                       list or dic
"""


def printAllFunctionInputList(*arg):
    inputLen = len(arg)
    for i in range(inputLen):
        print(arg[i], end=", ")
    print("\nend of printAllFunctionInputList function")
    print("-------------------------------------------")


def printAllFunctionInputDic(**arg):
    dicKeys = []
    for i in arg.keys():
        dicKeys.append(i)
        print(arg[i])


printAllFunctionInputList("amir", "bishoy", "bassam", "khilifa")
printAllFunctionInputDic(first="red", second="yellow", third="green")
