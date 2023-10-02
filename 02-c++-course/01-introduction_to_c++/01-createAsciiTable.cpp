/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-09-30 23:58:08
 * @ As Known As: DarkStar0x714
 * @ Description: simple program to print ascii table
 */

#include <iostream>
#include <ostream>

int main(int argc, const char** argv) {

    std::cout<<"ASCII Code Table:"<<std::endl;
    std::cout<<"+------+-------+"<<std::endl;
    std::cout<<"|" <<" Char "<<"|"<<" ASCII "<<"|"<<std::endl;
    std::cout<<"+------+-------+"<<std::endl;
    
    
for (int i = 0; i <= 127; ++i) {
        char character = static_cast<char>(i);
        std::cout << "|  ";
        if (i < 32) {
            // Handle control characters
            std::cout << "  " << "0" << "  |   " << i << "   |" << std::endl;
        } else {
            // Handle printable characters
            std::cout << character << "  |   " << i << "   |" << std::endl;
        }
    }

    std::cout << "+------+-------+" << std::endl;

    return 0;
}