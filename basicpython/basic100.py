import socket
host_name = socket.gethostname()
print("Host name:", host_name)
import platform
host_name = platform.uname()[1]
print("Host name:", host_name )
import os
host_name = os.uname().nodename
print("Host name:", host_name)


