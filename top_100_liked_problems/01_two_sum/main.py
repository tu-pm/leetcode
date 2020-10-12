# Two Sum
from collections import defaultdict

def twosum(nums, target):
    dd = defaultdict(list)
    for i, n in enumerate(nums):
        dd[n].append(i)
    for i in range(len(nums)):
        remain = target - nums[i]
        if remain in dd and dd[remain][0] != i:
            return i, dd[remain][0]
