#!/usr/bin/env python 

""" 
An echo server that uses select to handle multiple clients at a time. 
Entering any line of input at the terminal will exit the server.
""" 

import select 
import socket 
import sys 

host = '0.0.0.0' 
port = 50000 
backlog = 5 
size = 1024 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host,port)) 
server.listen(backlog) 
print 'start listennig ...'
input = [server,sys.stdin] 
running = 1 
while running: 
    inputready,outputready,exceptready = select.select(input,[],[]) 

    for s in inputready: 

        if s == server: 
            # handle the server socket 
            client, address = server.accept() 
            print 'accepted connection from %s'%str(address)
            input.append(client) 

        elif s == sys.stdin: 
            # handle standard input 
            print 'exiting ...'
            junk = sys.stdin.readline() 
            running = 0 


        else: 
            # handle all other sockets 
            data = s.recv(size) 
            print 'recieved data from client %s => %s'%(str(address),data)
           
            if data: 
               # s.send(data) 
                client.send('\n Data sent : %s' %data)
            else: 
            
                print 'Client leaving .. %s'%str(address)
                s.close() 
                input.remove(s) 
server.close()