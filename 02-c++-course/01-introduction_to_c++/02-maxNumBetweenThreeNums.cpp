/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-09-30 23:58:08
 * @ As Known As: DarkStar0x714
 * @ Description: simple program return the max number between three inputs
 */

#include <algorithm>
#include <iostream>

int main(int argc, const char** argv) {
    double num1=0;
    double num2=0;
    double num3=0;

    std::cout << "Enter 3 number to compare" << std::endl;
    
    std::cin>>num1>>num2>>num3;

    std::cout << std::max(std::max(num1,num2),num3) << std::endl;
    return 0;
}