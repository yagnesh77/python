d={1:70,2:80,3:90}
d1={}
def check(a):
    if a.values():
        print("dict is not empty :-"+'%s '%d)
    else:
        print('Empty')

check(d)
check(d1)