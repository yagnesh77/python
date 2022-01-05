s1 ={1,2,3,4,5,6,77,777,776}
s2 ={1,2,3,4,5}
s3 ={1,2,3,4,5,55}
s4 ={1,2,3,4,5,6,77,777}
print(s1.issuperset(s2))
print(s1.issuperset(s4))
print(s3.issuperset(s2))
print(s4.issuperset(s2))
print(s4.issuperset(s1))
