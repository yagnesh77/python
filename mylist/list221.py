from copy import deepcopy
from random import randint
def shuffle_list(lst):
  temp_lst = deepcopy(lst)
  m = len(temp_lst)
  while (m):
    m -= 1
    i = randint(0, m)
    temp_lst[m], temp_lst[i] = temp_lst[i], temp_lst[m]
  return temp_lst
nums = [1, 2, 3, 4, 5, 6]
print("Original list: ",nums)
print("\nShuffle the elements of the said list:")
print(shuffle_list(nums))
