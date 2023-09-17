#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     17 sep 2023
   Description   :     simple program to use api to suggest tasks to do when i am bored
"""

import requests

print(requests.get("https://www.boredapi.com/api/activity").json()
      ["activity"])
