def unfold(fn, seed):
  def fn_generator(val):
    while True:
      val = fn(val[1])
      if val == False: break
      yield val[0]
  return [i for i in fn_generator([None, seed])]
f = lambda n: False if n > 40 else [-n, n + 10]
print(unfold(f, 10))
