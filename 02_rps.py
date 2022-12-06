#!/usr/bin/env python3

def f(c: str, s: str) -> str:
    i = 0
    if s == 'X':   i = 2
    elif s == 'Y': i = 1
    return {
        'A': ('Y', 'X', 'Z'), 'B': ('Z', 'Y', 'X'), 'C': ('X', 'Z', 'Y'),
    }[c][i]

with open('02.in') as t:
    s = 0
    for p in t.read().split('\n'):
        a, _, c = p
        c = f(a, c)
        if any(((a == 'A' and c == 'X'), (a == 'B' and c == 'Y'), (a == 'C' and c == 'Z'))):   s += 3
        elif any(((a == 'A' and c == 'Y'), (a == 'B' and c == 'Z'), (a == 'C' and c == 'X'))): s += 6
        s += 1 if c == 'X' else (2 if c == 'Y' else (3 if c == 'Z' else 0))
    print(s)