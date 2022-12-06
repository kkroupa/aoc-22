#!/usr/bin/env python3

with open('01.in') as f:
    t = f.read()
    print(max(tuple(map(lambda elf: sum(map(int, elf.split('\n'))), t.rstrip('\n').split('\n\n')))))
    print(sum(sorted(tuple(map(lambda elf: sum(map(int, elf.split('\n'))), t.rstrip('\n').split('\n\n'))))[-3:]))