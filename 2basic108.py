def check_last_digit(x, y, z):
  return str(x*y)[-1] == str(z)[-1]

print(check_last_digit(12, 22, 44))
print(check_last_digit(145, 122, 1010))
print(check_last_digit(0, 22, 40))
print(check_last_digit(1, 22, 40))
print(check_last_digit(145, 122, 101))
