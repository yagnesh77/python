import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
print(list(itertools.chain(*original_list)))