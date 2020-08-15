# Problem: https://leetcode.com/problems/integer-to-roman/
def int2roman(num):
    res = ""
    mappings = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))
    for base, char in mappings:
        n_chars, num = divmod(num, base)
        res += n_chars * char
    return res
