#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     17 sep 2023
   Description   :     simple program to use api to get my public ip
"""

import requests

print(
    f'your ip is ------>{requests.get("https://api.ipify.org/?format=json").json()["ip"]}')
