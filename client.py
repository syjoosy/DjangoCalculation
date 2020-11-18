import socket

conn = socket.socket()
conn.connect(("0.0.0.0", 14900))
conn.send(b"I'm client! \n")
data = b""
tmp = conn.recv(1024)
while tmp:
    data += tmp
    tmp = conn.recv(1024)
print(data.decode("utf-8"))
conn.close()