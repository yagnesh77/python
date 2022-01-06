a='yagnesh'
if type(a)==int:
    print('its an integer')
elif type(a)==str:
    print('Its a string')
else:
    pass

#or
print()
print(isinstance(25,int) or isinstance(25,str))

print(isinstance([25],int) or isinstance([25],str))

print(isinstance("25",int) or isinstance("25",str))
