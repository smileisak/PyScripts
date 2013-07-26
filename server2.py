# Echo server program
import socket

HOST = '0.0.0.0'           # Symbolic name meaning the local host
PORT = 50003             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
print "Starting ECHO output ..."
data = 'dummy'
while len(data):
    data = conn.recv(1024)
    print 'receved msg ', data
    if not data: break
    conn.send(data)

print 'closing connection ...'
conn.close()
