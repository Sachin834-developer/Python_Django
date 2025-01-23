"""Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
    """


def find_pairs(lst, target):
    seen = set()
    pairs = set()
    for num in lst:
        bal = target - num
        if bal in seen:
            pairs.add(tuple((min((bal, num)), max(bal, num))))
        seen.add(num)
    return pairs


# effecient solun to return indecies
def twoSum(nums, target):
    num_to_index = {}  # Dictionary to store value-to-index mapping

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]  # Return indices of the two numbers
        num_to_index[num] = i  # Add the current number and its index to the dictionary

    return []  # Return an empty list if no solution exists


"""Time Complexity: 

O(n), where 

n is the length of the array. We iterate through the array once, and dictionary operations (insertion and lookup) take 

O(1) on average.
Space Complexity: 

O(n), for storing the dictionary.
    """
