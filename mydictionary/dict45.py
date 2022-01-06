d={'Cierra Vega': 10, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
v=list(d.values())[0]
count=0
for i in d.values():
   if i == v:
       count+=1
   else:
       pass

if count==len(d.values()):
    print(True)
else:
    print(False)