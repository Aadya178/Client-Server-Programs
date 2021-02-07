import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_host=socket.gethostname()
udp_port=6789
sock.bind((udp_host,udp_port))
print("Waiting for Client")
while True:
    data,addr=sock.recvfrom(1024)
    print("Received message:",data,"from",addr)
sock.close()