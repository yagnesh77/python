import glob
file_list = glob.glob('*.*')
print(file_list)
#Specific files
print(glob.glob('basic111.py'))
print(glob.glob('./[0-9].*'))
