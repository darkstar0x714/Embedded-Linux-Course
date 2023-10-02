/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-10-01 00:50:08
 * @ As Known As: DarkStar0x714
 * @ Description:  simple program to detect weather the input char is vowel or not
 */

#include <cctype>
#include <iostream>

int main(int argc, const char** argv) {
 char c;
 while (std::tolower(c)!='q')
 {
    std::cout << "enter char to check or q to exit" << std::endl;
    std::cin>>c;
    c=tolower(c);
    if (c=='a'||c=='e'||c=='o'||c=='u'||c=='i')
    {
        std::cout << "the entered char is vowel" << std::endl;
    }
    else
    {
        std::cout << "the entered char is not vowel" << std::endl;
        
    }
 }
    return 0;
}

