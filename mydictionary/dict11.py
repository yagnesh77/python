d1 = {'data1':100,'data2':200,'data3':2}
multi = 1
for i in d1.values():
    multi*=i
print(multi)

#or

my_dict = {'data1':100,'data2':-54,'data3':247}
result=1
for key in my_dict:
    result=result * my_dict[key]

print(result)
