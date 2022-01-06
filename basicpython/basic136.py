import os
print([f for f in os.listdir('/home/yagnesh/PycharmProjects/pythonProject') if os.path.isfile(os.path.join('/home/yagnesh/PycharmProjects/pythonProject', f))])
