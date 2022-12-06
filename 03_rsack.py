#!/usr/bin/env python3

from string import ascii_lowercase, ascii_uppercase
from functools import reduce

with open('03.in') as f:
    a = {v: k for k, v in enumerate(ascii_lowercase + ascii_uppercase, start = 1)}
    t = f.read().split('\n')
    x, y = 0, 0
    for r in t:
        c = len(r) // 2
        x += sum(map(lambda it: a[it], set.intersection(set(r[:c]), set(r[c:]))))
    for r in zip(*[iter(t)] * 3):
        y += sum(map(lambda it: a[it], set.intersection(reduce(set.intersection, map(set, r)))))
    print(x, y)