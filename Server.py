import socket
import time
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=1234
serversocket.bind((host,port))
serversocket.listen(5)
print("Waiting for Client")
while True:
    clientsocket,addr=serversocket.accept()
    print("Received connection from %s" %str(addr))
    currentTime=(time.ctime(time.time())+"\r\n")
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
serversocket.close()