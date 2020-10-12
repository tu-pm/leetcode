from test import gen_test, Watcher
import numpy as np

# DP approach: The initialization process costs even more than the actual
# computing procedure.
def dp(s):
    n = len(s)
    p = [[((j == i) or (j == i+1)) and s[i] == s[j] for j in range(n)]
             for i in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(i+2, n):
            p[i][j] = p[i+1][j-1] and s[i] == s[j]

    max_val, max_len = "", 0
    for i in range(n):
        for j in range(i, n):
            if p[i][j] and j-i+1 > max_len:
                max_len = j-i+1
                max_val = s[i:j+1]

    return max_val

# DP using numpy: You can use numpy arrays to speed up the initialization
# process. But since numpy only works well with parallelizable algorithms, you
# must convert the initiated array to a nested list, or else you'll get even
# worse performance than before.
def dp_numpy(s):
    n = len(s)

    p = np.identity(n, dtype=bool)
    for i in range(n-1):
        p[i,i+1] = (s[i] == s[i+1])
    p = p.tolist()

    for i in range(n-1, -1, -1):
        for j in range(i+2, n):
            p[i][j] = p[i+1][j-1] and s[i] == s[j]

    max_val, max_len = "", 0
    for i in range(n):
        for j in range(i, n):
            if p[i][j] and j-i+1 > max_len:
                max_len = j-i+1
                max_val = s[i:j+1]

    return max_val

# Expand edges: From a seed string, such as "a" or "aa", expand it both ways
# to get the largest palindromic substring from it. Then compare the substring
# resulted by performing this method on all possible center strings from s.
# Space complexity: O(1). Time complexity: O(n^2)
def expand_edges(s):
    max_val, max_len, n = "", 0, len(s)

    def longest_palindromic_substr(s, left, right):
        while True:
            if left == -1 or right == len(s) or s[left] != s[right]:
                return left+1, right-1
            left -= 1
            right += 1

    def update_max(s, left, right):
        nonlocal max_val, max_len
        if right - left + 1 > max_len:
            max_val = s[left:right+1]
            max_len = right-left+1

    for i in range(n):
        update_max(s, *longest_palindromic_substr(s, i, i))
        if i < n-1 and s[i] == s[i+1]:
            update_max(s, *longest_palindromic_substr(s, i, i+1))

    return max_val


if __name__ == '__main__':
    s = gen_test(1000, 667)
    res = expand_edges(s)
    print(res)
