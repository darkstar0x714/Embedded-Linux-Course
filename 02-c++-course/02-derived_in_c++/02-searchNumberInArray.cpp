/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-11-25 01:06:21
 * @ As Known As: DarkStar0x714
 * @ Description:  code to find user input element using c & c++ style coding
 */

#include <bits/stdc++.h>

int cStyleFindFunction(int element, int arr[], int arrSize)
{
    int ans = -1;

    for (int i = 0; i < arrSize; i++)
    {
        if (element == arr[i])
        {
            ans = i;
            break;
        }
    }
    return ans;
}

void cppStyleFindFunction(std::vector<int> vec, int element)
{

    auto it = std::find(vec.begin(), vec.end(), element);
    if (it != vec.end())
        std::cout << "Element found at index: " << std::distance(vec.begin(), it) << std::endl;
    else
        std::cout << "Element not found.";
}

int main()
{
    int arr[] = {1, 2, 3, 5, 7, 9, 4545, 4, 8, 10};
    int arraySize = sizeof(arr) / sizeof(arr[0]);

    int userInput;

    std::cout << "enter number to search for to return it's index";
    std::cin >> userInput;

    ((cStyleFindFunction(userInput, arr, arraySize)) > 0) ? std::cout << "element found in index " << cStyleFindFunction(userInput, arr, arraySize) << std::endl : std::cout << "element not found" << std::endl;

    std::vector<int> vec = {10, 20, 30, 40};

    cppStyleFindFunction(vec, 30);
}
