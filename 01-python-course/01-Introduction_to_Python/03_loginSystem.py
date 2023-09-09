#!/usr/bin/python3
""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     simple login system to show case dic usage and
                       perform some flow control
"""
from termcolor import colored

data_base = {
    "Ahmed": "1394",
    "Ali": "6078",
    "Amr": "9345"
}

userName = input("please enter user name :")

if userName in data_base.keys():
    passCode = input("please enter passcode :")
    if passCode == data_base[userName]:
        print(colored(f"welcome {userName}", "green"))
    else:
        print(colored("password not correct try agin", "red"))


else:
    print(colored("user not registed", "red"))
