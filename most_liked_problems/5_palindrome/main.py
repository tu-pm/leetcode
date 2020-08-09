from test import gen_test, Watcher
import numpy as np


def longestPalindrome(s):
    n = len(s)
    w = Watcher()
    p = [[((j == i) or (j == i+1)) and s[i] == s[j] for j in range(n)]
         for i in range(n)]
    w.watch()

    for i in range(n-1, -1, -1):
        for j in range(i+2, n):
            p[i][j] = p[i+1][j-1] and s[i] == s[j]
    w.watch()

    max_val, max_len = "", 0
    for i in range(n):
        for j in range(i, n):
            if p[i][j] and j-i+1 > max_len:
                max_len = j-i+1
                max_val = s[i:j+1]
    w.watch()
    return max_val

def longestPalindromeNumpy(s):
    n = len(s)
    w = Watcher()
    p = np.identity(n, dtype=bool)
    for i in range(n-1):
        p[i,i+1] = (s[i] == s[i+1])
    w.watch()

    for i in range(n-1, -1, -1):
        for j in range(i+2, n):
            p[i,j] = p[i+1,j-1] and s[i] == s[j]
    w.watch()

    max_val, max_len = "", 0
    for i in range(n):
        for j in range(i, n):
            if p[i,j] and j-i+1 > max_len:
                max_len = j-i+1
                max_val = s[i:j+1]
    w.watch()
    return max_val

s = gen_test(5000, 667)
res = longestPalindrome(s)
print("========================")
res = longestPalindromeNumpy(s)
