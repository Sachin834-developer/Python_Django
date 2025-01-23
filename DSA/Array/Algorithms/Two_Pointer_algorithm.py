"""
    TWO -POINTERS OR SQUEEZING Algorithm'
    
    USES: In-place manipulation on SORTED arrays (e.g., removing duplicates)
    
Generally for any array will consider 2 indecies one from the beggining of the array left = 0 and one at the end of the array right =0
    
    Ex 1:
    Square of a Sorted Array

    Problem: Given a sorted array of integers, return an array of the squares of each number, sorted in non-decreasing order.

    Input: [-4, -1, 0, 3, 10]
    Output: [0, 1, 9, 16, 100]
    
    """

input = [-4, -1, 0, 3, 10]


def sort_lst(lst):
    left = 0
    right = len(lst) - 1
    result = []
    while left <= right:
        if lst[left] > lst[right]:
            result.append(lst[left] ** 2)
            left += 1
        else:
            result.append(lst[right] ** 2)
            right -= 1
    return result[::-1]


print(sort_lst(input))
