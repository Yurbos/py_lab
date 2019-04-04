#!/usr/bin/python
import os
import sys


f = []
d = []
l = []

with os.scandir(sys.argv[1]) as i:
    for entry in i:
        if entry.is_file():
            f.append(entry.name)
        if entry.is_dir():
            d.append(entry.name)
        if entry.is_symlink():
            l.append(entry.name)


f.sort()
d.sort()
l.sort()


for x in range(len(d)):
    print("Dir\t", d[x])

for x in range(len(f)):
    print("File\t", f[x])

for x in range(len(l)):
    print("Link\t", l[x])
