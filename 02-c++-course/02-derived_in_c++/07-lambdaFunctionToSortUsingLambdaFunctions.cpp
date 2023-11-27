/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-11-27 04:11:04
 * @ As Known As: DarkStar0x714
 * @ Description: simple code to use lambda functions to sort vector ascending and descending
 */

#include <bits/stdc++.h>

int main()
{
    std::vector<int> vec;

    std::cout << "enter any number to add to vector or 0 to sort" << std::endl;

    while (1)
    {
        int temp;
        std::cin >> temp;
        if (temp != 0)
        {
            vec.push_back(temp);
        }
        else
        {
            break;
        }
    }

    std::cout << "the descending order of the vector is : ";

    std::sort(vec.begin(), vec.end(), [](int a, int b)
              { return a > b; });

    for (auto &&i : vec)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    std::cout << "the ascending order of the vector is : ";

    std::sort(vec.begin(), vec.end(), [](int a, int b)
              { return a < b; });

    for (auto &&i : vec)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}