import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_host=socket.gethostname()
udp_port=6789
print("UDP target IP:", udp_host)
print("UDP target port:", udp_port)
message=""
while message!="bye":
    message=input()
    sock.sendto(message.encode(),(udp_host,udp_port))