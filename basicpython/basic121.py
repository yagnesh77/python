try:
    x = 7
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")
try:
    y
except NameError:
    print("Variable is not defined....!")
else:
    print("Variable is defined.")
