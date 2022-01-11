from random import choice
with open('file1.py') as f:
    l=f.read().split()
    print(choice(l))