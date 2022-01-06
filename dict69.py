from collections import defaultdict
from math import floor
def test(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
nums = [7,23, 3.2, 3.3, 8.4]
print("Group the elements of the said list based on the given function:")
print(test(nums, floor))
print("\n")
colors = ['Red', 'Green', 'Black', 'White', 'Pink']
print("Group the elements of the said list based on the given function:")
print(test(colors, len))