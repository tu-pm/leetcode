# Add Two Numbers
from itertools import zip_longest
def add(l1, l2):
    res, pad = [], 0
    for d1, d2 in zip_longest(l1, l2, fillvalue=0):
        total = d1 + d2 + pad
        pad = total // 10
        res.append(total % 10)
    return res
