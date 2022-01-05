str1=input('Enter a string: ')
copies=int(input('Enter a num: '))
if len(str1)<2:
    print(copies*str1)
else:
    print(copies*str1[0:2])


   