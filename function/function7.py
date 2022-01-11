s1='The quick Brow Fox'
def fu(s1):
    c1,c2=0,0
    for i in s1:
        if i.isupper():
            c1+=1
        elif i.islower():
            c2+=1
    return (c1,c2)
print(fu(s1))