result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (column == 1 or (row == 6 and column != 0 and column < 6)):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str);
