#!/usr/bin/python3
""" 
   Author        :     Amir W. Fathy
   Date          :     17 sep 2023
   Description   :     create .cpp and .h files with given name with a starter code
"""

fileName = input("Enter cpp file name ")
cppFile = open(f"{fileName}.cpp", "w+")

codeTemp = """
/*\n
this is an auto generated code from python extension\n
*/\n\n
#include <iostream>\n
int main() {\n
    std::cout << "Hello, World!" << std::endl;\n
    return 0;\n
}\n"""

cppFile.write(codeTemp)

hFile = open(f"{fileName}.h", "w+")

headerTemp = f"""
#ifndef _{fileName.upper()}_H_\n
#define _{fileName.upper()}_H_\n

// Declarations for your functions, classes, or variables go here\n

#endif \n

"""

hFile.write(headerTemp)
