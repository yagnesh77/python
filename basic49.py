from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/yagnesh/PycharmProjects/pythonProject/Basic') if isfile(join('/home/yagnesh/PycharmProjects/pythonProject/Basic',f))]
print(files_list);