def search(nums, target, start, end):
    # Not found
    if start == end and nums[start] != target:
        return -1, -1
    # All numbers from start to end equals target
    if nums[start] == nums[end] and nums[start] == target:
        return start, end
    mid = (start + end) // 2
    # Search right
    if nums[mid] < target:
        return search(nums, target, mid + 1, end)
    # Search left
    if nums[mid] > target:
        return search(nums, target, start, mid)
    left, _ = search(nums, target, start, mid)
    _, right = search(nums, target, mid + 1, end)
    if right == -1:
        return left, mid
    return left, right

nums = [5,7,7,8,8,10]
print(search(nums, 8, 0, len(nums) - 1))
