#!/usr/bin/env python


import socket
import sys 


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpsock.connect((sys.argv[1],50003))

while True:
	userInput = raw_input('Enter a string : ')
	tcpsock.send(userInput)
	print 'recieved DATA => %s'%tcpsock.recv(1024)

tcpsock.close() 