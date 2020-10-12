# Problem: https://leetcode.com/problems/3sum-closest/
from collections import Counter


def three_sum(nums, target):
    nums = sorted(nums)
    closest = (2 << 31) - 1
    for i in range(len(nums) - 2):
        begin, end = i + 1, len(nums) - 1
        while begin < end:
            total = nums[i] + nums[begin] + nums[end]
            if abs(total - target) < abs(closest - target):
                closest = total
            if total < target:
                begin += 1
            else:
                end -= 1
    return closest


print(three_sum([0, 0, 0], 1))
