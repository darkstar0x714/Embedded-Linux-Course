/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-10-01 21:28:54
 * @ As Known As: DarkStar0x714
 * @ Description:  simple program to take var from user and print the multiplication table
 */

#include <iostream>
#include <iterator>
int main(int argc, const char** argv) {

    int var;
    std::cout << "enter a number to print it's table" << std::endl;
    std::cin>>var;
    std::cout<< "the multiplication table is :-" <<std::endl;

    for (int i = 0; i <= 12; i++)
    {
        std::cout << i<<"x"<<var<<" = "<<i*var << std::endl;
    }
    return 0;
}
