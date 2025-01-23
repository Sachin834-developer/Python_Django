lst = [1, 2, 3, -2, 5]
# lst=[-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_sum_subarr(nums: list[int]) -> int:
    max_sum = 0
    cur_sum = 0
    for num in nums:
        cur_sum = max(num, num + cur_sum)
        max_sum = max(cur_sum, max_sum)
    return max_sum


print(max_sum_subarr(lst))
