import socket
s=socket.socket()
host=socket.gethostname()
port=1111
s.connect((host,port))
print("Client waiting for connection to server")
s.send("request for connection".encode())
while True:
    data=s.recv(1024)
    if data.decode()=='bye' or not data:
        break
    print("Server: "+data.decode())
    data=input("Client: ")
    s.sendall(data.encode())
s.close()