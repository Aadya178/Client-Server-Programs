import socket
s=socket.socket()
host=socket.gethostname()
port=1111
s.bind((host,port))
s.listen(5)
print("Waiting for 1 connection")
conn,addr=s.accept()
print("Client has connected")
conn.send("Welcome to the server".encode())
while True:
    data=conn.recv(1024)
    if data.decode()=='bye' or not data:
        break
    data=data.decode()
    print("Client: "+data)
    data=input("Server: ")
    conn.sendall(data.encode())
s.close()