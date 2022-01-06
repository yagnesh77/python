def intcheck(a, b):
  if type(a) == int and type(b) == int:
    sum = a + b
    return sum
  else:
    return 'objects are not integer.'


print(intcheck(1, 2.5))
print(intcheck(1, 2))
print(intcheck('1', 2.5))
print(intcheck(1, 'yagnesh'))



