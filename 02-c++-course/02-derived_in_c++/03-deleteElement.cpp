/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-11-25 20:15:26
 * @ As Known As: DarkStar0x714
 * @ Description: example to delete element from vector
 */

#include <bits/stdc++.h>

int main()
{
    std::vector<int> vec = {1, 2, 3, 4, 5, 7};

    std::cout << "original array is" << std::endl;
    for (auto &&i : vec)
    {
        std::cout << i << " ";
    }
    std::cout << std::endl;

    int elementToBeRemoved;

    std::cout << "enter number to be removed from array";
    std::cin >> elementToBeRemoved;

    vec.erase(std::find(vec.begin(), vec.end(), elementToBeRemoved));
    std::cout << "editable array is" << std::endl;

    for (auto &&i : vec)
    {
        std::cout << i << " ";
    }
}