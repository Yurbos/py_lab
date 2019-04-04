import os
import sys


f = []
d = []
l = []

f_size = []
d_size = []
l_size = []


with os.scandir(sys.argv[1]) as i:
    for entry in i:
        if entry.is_file():
            f.append(entry.name)
            f_size.append(os.path.getsize(entry.path))
        if entry.is_dir():
            d.append(entry.name)

            def get_size(start_path=entry.path):
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
            d_size.append(get_size())
        if entry.is_symlink():
            l.append(entry.name)

for x in range(len(d)):
    print("Dir\t", d_size[x],"\t", "\t", d[x])

for x in range(len(f)):
    print("File\t", f_size[x],"\t", "\t", f[x])

for x in range(len(l)):
    print("Link\t", "\t", "\t", l[x])
