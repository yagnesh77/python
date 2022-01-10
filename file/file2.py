fname=input('Enter a file: ')
from itertools import islice
with open(fname) as f:
    for line in islice(f, 2):
            print(line)
