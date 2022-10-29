import socket
import re

ip = input("Enter the IP address of the server: 192.168.")
if ip != "":
    ip = "192.168." + ip
else:
    ip = input("Enter the IP address of the server:")
#TCP_IP = '176.9.20.205'
#TCP_IP = '192.168.0.2'


BUFFER_SIZE = 550

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 25565))
s.send(b"\xfe")  # Minecraft server ping packet
data = s.recv(BUFFER_SIZE)
s.close()

assert data[0] == 255  # test for valid response
info = data[3:].split(b"\xa7")  # split the data into a list

for i in range(len(info)):
    info[i] = info[i].decode("ascii", errors="replace")
    info[i] = info[i].replace("\x00", "")

print("############################################")
print("Ping response from " + ip + ":")
print(info[0], f"[{info[1]}/{info[2]}]")
print("############################################")
