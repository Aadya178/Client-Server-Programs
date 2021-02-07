import socket  
s = socket.socket()             
host = socket.gethostname()     
port = 65122
s.connect((host, port))
s.send("Hello Server".encode())
with open("recv_file.txt", 'w') as f:
    print("File opened")
    print("Receiving data")
    print("Server:")
    while True:
        data = s.recv(1024)
        data=data.decode()
        data=str(data)
        if not data:
            break
        print(str(data))
        f.write(data)
#f.close()
print("File received")
s.close()
print("Connection closed")