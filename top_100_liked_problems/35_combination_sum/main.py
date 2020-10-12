class Result(object):
    def __init__(self):
        self.items = []
        self.total = 0

    def add(self, value):
        self.items.append(value)
        self.total += value

    def pop(self):
        self.total -= self.items[-1]
        self.items = self.items[:-1]

def combination(candidates, target):
    candidates = sorted(candidates)
    solutions = []
    sol = Result()

    def backtrack(k):
        for i in range(k, len(candidates)):
            if sol.total + candidates[i] > target:
                break
            sol.add(candidates[i])
            if sol.total == target:
                solutions.append(sol.items)
            else:
                backtrack(i)
            sol.pop()

    backtrack(0)
    return solutions

candidates = [1, 2]
target = 2
print(combination(candidates, target))
