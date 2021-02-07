import socket                   
import subprocess
s=socket.socket()
host=socket.gethostname()
port=65112
s.connect((host,port))
while True:
    c=s.recv(1024).decode()
    user_cmd=input(c)
    s.send(user_cmd.encode())
    if user_cmd=="exit":
        break
    disp=s.recv(1024).decode()
    print(disp)
s.close()