#!/usr/bin/env python

import socket
tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
tcpSocket.bind(("0.0.0.0",8000))
tcpSocket.listen(2)

print 'waiting for a Client ...'

(client,(ip,port)) =tcpSocket.accept()
print "receved connection from " ,ip
print "Starting ECHO output ..."
data = 'dummy'
while len(data):
	data = client.recv(2048)
	print "client send ", data 
	client.send(data)
print 'closing connection ...'
client.close()
