/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-11-25 23:29:12
 * @ As Known As: DarkStar0x714
 * @ Description: simple code to use lambda functions to get sqr of an user input number
 */

#include <bits/stdc++.h>

int main()
{
    int number;
    std::cout << "enter number to print square root " << std::endl;
    std::cin >> number;
    auto square = [number]()
    { return number * number; };

    std::cout << square() << std::endl;
}