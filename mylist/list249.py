def min_by(lst, fn):
  return min(map(fn, lst))
print(min_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']))
