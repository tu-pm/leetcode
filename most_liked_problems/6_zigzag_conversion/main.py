from math import ceil
def convert(s, numRows):
    if numRows == 1:
        return s
    n = len(s)
    numCols = ceil(n/(numRows - 1))
    res = ['' for _ in range(numRows * numCols)]
    for pos, char in enumerate(s):
        a, b = pos // (numRows-1), pos % (numRows-1)
        if a % 2 == 0:
            x, y = b, a
        elif b == 0:
            x, y = numRows-1-b, a-1
        else:
            x, y = numRows-1-b, a
        print(x, y)
        newPos = x * numCols + y
        res[newPos] = char
    return ''.join(res)

s="PAYPALISHIRING"
res = convert(s, 4)
print(res)
