import os
import sys
import random
import string
import shutil

root_dir = sys.argv[1]+"fun"

os.mkdir(root_dir)
os.chdir(root_dir)

text = open('some.txt', 'w')

type = ['Dir', 'File']

for x in range(random.randint(2, 10)):
    text.write(str(random.choice(type)) + '\n')

text.close()


text = open('some.txt', 'r')
t = [line.strip() for line in text]
text.close()

print(t)


def randomstring(stringlength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringlength))


for x in t:
    if x == 'Dir':
        d = randomstring(7)
        os.mkdir(root_dir+'\\'+d)
        print(x, "Found")
    if x == 'File':
        f = randomstring(7)
        os.chdir(root_dir+'\\'+d)
        text = open(f+'.txt', 'w')
        os.chdir(root_dir + '\\' + d)
        text.close()
        os.chdir(root_dir)
        print(x, "Found")

shutil.rmtree(root_dir, ignore_errors=True)