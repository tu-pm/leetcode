# Problem: https://leetcode.com/problems/3sum/
from collections import Counter


def three_sum(nums):
    counter = sorted(Counter(nums).items())
    items = set(item[0] for item in counter)
    results = set()
    for i, item in enumerate(counter):
        first, count = item
        # Three items in the triplet are equal, i.e. all are zeros.
        if first == 0 and count >= 3:
            results.add((0, 0, 0))
        # Two out of three items in the triplet are equal.
        if first != 0 and count >= 2 and (-2 * first) in items:
            results.add((first, first, -(2 * first)))
        # All three items are different. Make sure they are in ascending order two eliminate duplicates
        for second, _ in counter[i + 1:]:
            third = - first - second
            if third in items and third > max(first, second):
                results.add((first, second, third))
    return [list(x) for x in results]


print(three_sum([3, 0, -2, -1, 1, 2]))
