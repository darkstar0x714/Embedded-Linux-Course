/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-11-25 22:55:43
 * @ As Known As: DarkStar0x714
 * @ Description: code to print even and odd elements
 */

#include <bits/stdc++.h>

int main()
{
    std::vector<int> userInput;
    std::vector<int> oddVector;
    std::vector<int> evenVector;

    std::cout << "enter int numbers and press enter to add press '0' to process the data" << std::endl;
    while (1)
    {
        int element;
        std::cin >> element;
        if (element != 0)
        {
            userInput.push_back(element);
        }
        else
        {
            break;
        }
    }

    for (auto &&i : userInput)
    {
        if (i % 2 == 0)
        {
            evenVector.push_back(i);
        }
        else
        {
            oddVector.push_back(i);
        }
    }

    std::cout << "even numbers is ";
    for (auto &&i : evenVector)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    std::cout << "odd numbers is ";
    for (auto &&i : oddVector)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}