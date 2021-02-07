import socket                   
s = socket.socket()            
host = socket.gethostname()
port = 65122
s.bind((host, port))            
s.listen(5)
print("Waiting for Client")
while True:
    conn, addr = s.accept()
    conn.send("Hello Client".encode())
    print("Client connected")
    data = conn.recv(1024)
    print("Client:"+data.decode())
    filename=input()
    f = open(filename,'r')
    l = f.read(1024).encode()
    while (l):
        conn.send(l)
        print('Server:',l)
        l = f.read(1024).encode()
    f.close()
    print("File transferred")
    conn.send("Thank you for connecting".encode())
    conn.close()