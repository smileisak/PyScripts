#!/usr/bin/env python

import socket
import threading
import time

class myServer(threading.Thread):
    def __init__(self, ip , port , clientsock):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port 
        self.clientsock = clientsock 
        print "[+] New thread started for "+ip+":"+str(port)
 
    def run(self):
    	print "Connection from : "+ip+":"+str(port)
    	clientsock.send("\nWelcome to the server\n\n")
    	print 'Starting ECHO output : '
    	data = 'dummy'
    	while len(data):
    		data = clientsock.recv(1024)
    		print 'Recieved DATA from client %s: %s '%(ip ,data)
    		clientsock.send(data)
    	print "Client disconnected..."


HOST = '0.0.0.0'
PORT = 50003         
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print "Starting.. "
tcpsock.bind((HOST, PORT))
threads = []
while True:
	tcpsock.listen(4)
	print "\nListening for incoming connections..."
	(clientsock, (ip, port)) = tcpsock.accept()
	newthread = myServer(ip, port, clientsock)
	newthread.start()
	threads.append(newthread)


for t in threads:
	t.join()






