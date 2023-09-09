#!/usr/bin/python3
""" 
   Author         :     Amir W. Fathy
   Date          :     9 sep 2023
   Description   :     simple program print path environment variable using OS module
"""

import os

# get the value of the PATH environment variable
path = os.environ['PATH'].split(":")

for i in path:
    print(i)
