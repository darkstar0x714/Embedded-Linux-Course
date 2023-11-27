/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-11-25 22:48:44
 * @ As Known As: DarkStar0x714
 * @ Description: code to merge 2 arrays
 */

#include <bits/stdc++.h>

int main()
{
    std::vector<int> vec1 = {1, 2, 3, 4};
    std::vector<int> vec2 = {5, 6, 7, 8};

    vec1.insert(vec1.end(), vec2.begin(), vec2.end());

    for (auto &&i : vec1)
    {
        std::cout << i << " ";
    }
}