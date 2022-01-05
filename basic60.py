import math
acute=float(input('Enter acute angle: '))
obtuse=float(input('Enter obtuse angle: '))
hypothese=math.sqrt(acute**2+obtuse**2)
print('Hypothese of right angle is: {}'.format(hypothese))