from bisect import bisect_left

def binary_search(nums, target, start, end):
    pos = bisect_left(nums, target, start, end + 1)
    return pos if pos != end + 1 and nums[pos] == target else -1

def rotate_search(nums, target, start, end):
    mid = (start + end) // 2
    # Found target in the middle of nums
    if nums[mid] == target:
        return mid
    # Target not found
    if start == end:
        return -1
    # The right side is rotated
    if nums[mid] > nums[end]:
        if nums[mid] < target or nums[end] >= target:
            return rotate_search(nums, target, mid + 1, end)
        return binary_search(nums, target, start, mid)
    # The left side is rotated
    if nums[mid] < nums[start]:
        if nums[mid] > target or nums[start] =< target:
            return rotate_search(nums, target, start, mid)
        return binary_search(nums, target, mid + 1, end)
    # The array is sorted, use binary search
    return binary_search(nums, target, start, end)

