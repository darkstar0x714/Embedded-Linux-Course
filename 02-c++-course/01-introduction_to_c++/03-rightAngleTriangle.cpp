/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-09-30 23:58:08
 * @ As Known As: DarkStar0x714
 * @ Description: simple program to check if the input triangle is right angle or not by entering 3 sides length
 */

#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>

int main(int argc, const char** argv) {
    
    double sides[]={0,0,0};

    std::cout << "Enter three sides of a triangle" << std::endl;
    std::cin>>sides[0]>>sides[1]>>sides[2];

    std::sort(std::begin(sides),std::end(sides));

    if ((std::pow(sides[2],2))==(std::pow(sides[1],2))+(std::pow(sides[0],2)))
    {
        std::cout << "this is a right angle triangle" << std::endl;
    }
    else
    {
        std::cout << "this is not a right angle triangle" << std::endl;
        
    }
    return 0;
}