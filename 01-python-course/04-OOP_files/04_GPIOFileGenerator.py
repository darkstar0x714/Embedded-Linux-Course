#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     22 sep 2023
   Description   :     simple c code generator for avr GPIO driver
"""

DioRegister = []

for i in range(8):
    direction = input(f"Please enter Bit {i} mode: ")
    if direction == "in":
        DioRegister.append(0)
    else:
        DioRegister.append(1)

# Convert DioRegister to a binary string
binary_string = ''.join(map(str, DioRegister))

cFile = open("init.c", "w+")

codeTemp = f"""
/*
this is an auto-generated code from python extension
*/

void Init_PORTA_DIR (void)
{{
    DDRA = 0b{binary_string};
}}
"""

cFile.write(codeTemp)
cFile.close()

print("Code generation completed and saved to 'init.c'")
