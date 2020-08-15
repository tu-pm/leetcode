from time import time
from random import choices
from string import ascii_lowercase as letters

def gen_test(len_s, len_pal):
    len_pal  = min(len_pal, len_s)
    leftover = ''.join(choices(letters, k=len_s - len_pal))
    half_pal = ''.join(choices(letters, k=len_pal // 2))
    mid_char = ''.join(choices(letters, k=len_pal % 2))
    full_pal = half_pal + mid_char + half_pal[::-1]
    splitidx = choices(range(len_s - len_pal + 1), k=1)[0]
    result   = leftover[:splitidx] + full_pal + leftover[splitidx:]
    return result

class Watcher(object):
    def __init__(self):
        self.curr = time()
    def watch(self):
        last, self.curr  = self.curr, time()
        print(self.curr - last)

def watcher():
    curr = time()
    yield
    while True:
        last, curr = curr, time()
        yield print(curr - last)

def x(s):
    m = 3
    def y():
        nonlocal s, m
        s = 1
        m = 4
    y()
    print(s, m)
