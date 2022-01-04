import subprocess as sp
returned_text = sp.check_output("dir", shell=True, universal_newlines=True)
print(returned_text)
output = sp.getoutput('nano --version')
print (output)