import socket
s=socket.socket()
host=socket.gethostname()
port=64591
s.connect((host,port))
for i in range(3):
    ip_address=input("IP address whose MAC address is required:")
    s.send(ip_address.encode())
    mac_address=s.recv(1024).decode()
    print("MAC address for the corresponding IP address:",mac_address)
s.close()