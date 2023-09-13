#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     10 sep 2023
   Description   :     simple program get bitcoin price from api and print it in USD
"""

import requests

responseOfBitcoinPrice = requests.get(
    'https://api.coindesk.com/v1/bpi/currentprice.json')

# Check if the request was successful
if responseOfBitcoinPrice.status_code == 200:
    data = responseOfBitcoinPrice.json()
    print(f'price now in USD is = {data["bpi"]["USD"]["rate_float"]} $')
