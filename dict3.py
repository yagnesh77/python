dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for d in (dic1, dic2, dic3): dic4.update(d)
print(dic4)
#or
dic5={1:10, 2:20}
dic6={3:30, 4:40}
dic7={5:50,6:60}
dic8={**dic1,**dic2,**dic3}
print(dic8)