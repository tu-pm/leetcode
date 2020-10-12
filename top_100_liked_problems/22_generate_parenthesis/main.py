def parenthesis(n):
    result = []
    parens = [None] * 2 * n
    def backtrack(k, char, opens, closes):
        parens[k] = char
        if k == 2 * n - 1:
            result.append(''.join(parens))
        if opens < n:
            backtrack(k+1, '(', opens+1, closes)
        if closes < opens:
            backtrack(k+1, ')', opens, closes+1)
    backtrack(0, '(', 1, 0)
    return result

