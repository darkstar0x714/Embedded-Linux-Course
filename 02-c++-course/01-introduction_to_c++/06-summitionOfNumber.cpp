/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-10-01 21:36:11
 * @ As Known As: DarkStar0x714
 * @ Description:  simple program to sum all digits in given number 
 */

#include <iostream>

int main() {
    std::cout << "Enter an integer: ";
    int num;
    std::cin >> num;

    int sum = 0;

    while (num != 0) {
        int digit = num % 10;  
        sum += digit;         
        num /= 10;            
    }

    std::cout << "Sum of digits: " << sum << std::endl;

    return 0;
}
