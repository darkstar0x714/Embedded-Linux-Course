#!/usr/bin/python3
""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     simple program to print month calender and perform some basic operation on it like
                       (next month - next year - previous month - previous year)
                       with some error handling to verify user input 
"""

import calendar

Date = input("PLease Enter The date in the following format MM/YY : ")
Date = Date.split("/")


try:
    year = int(Date[1])
    month = int(Date[0])
    while 1:
        print(calendar.month(year, month))

        c = input("""for next month "nm"\n
                    for next year "ny"\n
                    for previous month "pm"\n
                    for previous year"py"\n
                    for exit "e"
                    """).lower()

        if c == "e":
            break

        elif (c == "nm") and ((month) < 12):
            month += 1
            print(calendar.month(year, month))

        elif (c == "nm") and ((month) == 12):
            month = 1
            year += 1
            print(calendar.month(year, month))

        elif (c == "pm") and ((month) > 1):
            month -= 1
            print(calendar.month(year, month))

        elif (c == "pm") and ((month) == 1):
            month = 12
            year -= 1
            print(calendar.month(year, month))

        elif c == "ny":
            year += 1
            print(calendar.month(year, month))

        elif c == "py":
            year -= 1
            print(calendar.month(year, month))

        else:
            print("\nwrong choice try again..")

except:
    print("please enter correct formula next time mm/yy EX 09/23")
