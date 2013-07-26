#!/usr/bin/env python

import multiprocessing 
import socket


class myserver(multiprocessing.Process):
   
    def __init__(self, ip , port , clientsock):
        multiprocessing.Process.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsock = clientsock

        
    def run(self):
        print "Connection from : "+ip+":"+str(port)
        clientsock.send("\nWelcome to the server\n\n")
        print 'Starting ECHO output : '
        data = 'dummy'
        while len(data):
            data = clientsock.recv(1024)
            print 'Recieved DATA from client %s with remote port %s: %s '%(ip, port,data)
            clientsock.send("\n sent data : %s "%data) 
        print "Client disconnected..."

HOST = '0.0.0.0'
PORT = 50003         
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print "Starting.. "
tcpsock.bind((HOST, PORT))
process = []
while True:
    tcpsock.listen(4)
    print "\nListening for incoming connections..."
    (clientsock, (ip, port)) = tcpsock.accept()
    newprocess = myserver(ip, port, clientsock)
    newprocess.start()
    process.append(newprocess)
