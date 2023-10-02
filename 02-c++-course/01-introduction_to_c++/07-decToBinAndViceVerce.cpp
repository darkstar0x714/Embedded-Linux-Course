/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-10-01 21:54:55
 * @ As Known As: DarkStar0x714
 * @ Description:  simple program to convert dec to bin and bin to dec.
 */
 
#include <iostream>
#include <bitset>
#include <string>

int main() {
    int number;
    char operation = 'd'; 

    std::cout << "Enter a number to convert: ";
    std::cin >> number;

    int check = number;

    while (check != 0) {
        int digit = check % 10;
        if (digit == 0 || digit == 1) {
            check /= 10;
        } else {
            operation = 'b';
            break;
        }
    }

    if (operation == 'b') {
        std::bitset<32> binaryBits(number); 
        std::string binaryString = binaryBits.to_string();
        std::cout << "Decimal: " << number << std::endl;
        std::cout << "Binary:  " << binaryString << std::endl;
    } else if (operation == 'd') {
        std::bitset<32> binaryBits(std::to_string(number)); 
        int decimalValue = static_cast<int>(binaryBits.to_ulong());
        std::cout << "Binary: " << number << std::endl;
        std::cout << "Decimal: " << decimalValue << std::endl;
    } 

    return 0;
}
