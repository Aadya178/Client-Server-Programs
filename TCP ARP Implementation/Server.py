from getmac import get_mac_address as g
import socket
s=socket.socket()
host=socket.gethostname()
port=64591
s.bind((host,port))
print("Waiting for connection")
s.listen(5)
conn,addr=s.accept()
for i in range(3):
    ip_address=conn.recv(1024).decode()
    print("IP address whose MAC address is required:",ip_address)
    ip_to_mac=g(ip=ip_address)
    ip_to_mac=bytes(ip_to_mac,'utf-8')
    conn.send(ip_to_mac)
conn.close()
s.close()