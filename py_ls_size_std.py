import os
import sys

root_dir = sys.argv[1]

print(root_dir)
f = []
d = []
l = []

f_size = []
d_size = []
l_size = []


def get_size(start_path):
    total_size = 0
    seen = {}
    for dirpath, dirnames, filenames in os.walk(start_path):
        for j in filenames:
            fp = os.path.join(dirpath, j)
            try:
                stat = os.stat(fp)
            except OSError:
                continue
            try:
                seen[stat.st_ino]
            except KeyError:
                seen[stat.st_ino] = True
            else:
                continue
            total_size += stat.st_size
    return total_size


def tofixed(numobj, digits):
    return f"{numobj:.{digits}f}"


def size_print(i):
    if i >= 1073741824:
        i = i / 1073741824
        result = str(tofixed(i, 3))+" GB"
        return result
    else:
        i = i / 1048576
        result = str(tofixed(i, 3)) + " MB"
        return result


with os.scandir(root_dir) as i:
    for entry in i:
        if entry.is_file():
            f.append(entry.name)
            f_size.append(os.path.getsize(entry.path))
        if entry.is_dir():
            d.append(entry.name)
            size = get_size(start_path=entry.path)
            d_size.append(size)
        if entry.is_symlink():
            l.append(entry.name)


for x in range(len(d)):
    print("Dir\t", size_print(d_size[x]),"\t", "\t", d[x])

for x in range(len(f)):
    print("File\t", size_print(f_size[x]),"\t", "\t", f[x])

for x in range(len(l)):
    print("Link\t", "\t", "\t", l[x])
