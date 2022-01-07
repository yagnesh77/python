s=[1, 3, 5, 7, 9, 10]
s1=[2, 4, 6, 8]
s.remove(s[-1])
s.extend(s1)
print(s)

#or

num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)