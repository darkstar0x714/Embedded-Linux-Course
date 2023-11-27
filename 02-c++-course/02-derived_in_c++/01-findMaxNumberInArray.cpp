/**
 * @ Author: Amir W. Fathy
 * @ Create Time: 2023-11-24 23:18:54
 * @ As Known As: DarkStar0x714
 * @ Description: code to find max number in array using c & c++ style coding
 */

#include <limits>
#include <bits/stdc++.h>

int *cStyleFindMaxElementInArray(int arr[], int arrSize, int ans[])
{
    int max = std::numeric_limits<int>::min();
    for (int i = 0; i < arrSize; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
            ans[0] = max;
            ans[1] = i;
        }
    }
    return ans;
}

std::pair<int, int> cppStyleFindMaxElementInArray(const std::vector<int> &arr)
{
    auto maxElement = std::max_element(arr.begin(), arr.end());
    int maxIndex = std::distance(arr.begin(), maxElement);

    return std::make_pair(*maxElement, maxIndex);
}

int main()
{
    int arr[] = {4, 5, 7, 3, 122, 1, 10, 15};
    int arraySize = sizeof(arr) / sizeof(arr[0]);
    int ans[2];
    int *answer = cStyleFindMaxElementInArray(arr, arraySize, ans);

    std::cout << "max element is = " << answer[0] << std::endl;
    std::cout << "max element index is = " << answer[1] << std::endl;

    std::vector<int> array = {4, 5, 7, 3, 122, 1, 10, 15};
    std::cout << "max element is = " << cppStyleFindMaxElementInArray(array).first << std::endl;
    std::cout << "max element index is = " << cppStyleFindMaxElementInArray(array).second << std::endl;
}
