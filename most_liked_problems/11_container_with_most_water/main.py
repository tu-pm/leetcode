# Problem: https://leetcode.com/problems/container-with-most-water/
# Solution:
# The area between two lines equals to the distance between them times the length of the shorter line.
# Start from to ends in the list, assume that the first line is shorter than the last line.
# In that case, the area between them is the largest area which the first line can produce.
# So we take it out of consideration and starts from the second line and so on.
def max_area(height):
    def area(begin, end):
        return (end - begin) * min(height[begin], height[end])

    def max_sub_area(begin, end):
        if end - begin == 1:
            return area(begin, end)
        elif height[begin] < height[end]:
            return max(area(begin, end), max_sub_area(begin+1, end))
        else:
            return max(area(begin, end), max_sub_area(begin, end-1))

    return max_sub_area(0, len(height) - 1)
