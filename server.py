import socket


sock = socket.socket()
sock.bind(("", 14900))
sock.listen(1)
conn, addr = sock.accept()
data = conn.recv(16384)
udata = data.decode("utf-8")
print("Data: " + udata)
conn.send(b"I'm server!\n")
conn.send(b"Your data: " + udata.encode("utf-8"))
conn.close()