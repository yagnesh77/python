result_str="";
for row in range(0,7):
    for column in range(0,7):
        if (column == 1 or ((row == 0 or row == 3) and column > 0 and column < 5) or ((column == 5 or column == 1) and (row == 1 or row == 2))):
            result_str=result_str+"*"
        else:
            result_str=result_str+" "
    result_str=result_str+"\n"
print(result_str);
