#!/usr/bin/env python


import socket
import struct
import binascii
import sys
rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

pkt= rawSocket.recvfrom(2048)

ethernetHeader = pkt[0][0:14]
eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)
binascii.hexlify(eth_hdr[0])
binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])

ipHeader =pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s", ipHeader)


#initial part of tcp header
tcpHeader = pkt[0][34:54]
tcp_hdr = struct.unpack('!HHLLBBHHH' , tcpHeader)
source_port = tcp_hdr[0]
dest_port = tcp_hdr[1]
sequence = tcp_hdr[2]
acknowledgement = tcp_hdr[3]
doff_reserved = tcp_hdr[4]
tcph_length = doff_reserved >> 4
data = pkt[0][54:]
if source_port == 443:
	
	print '[*]Source ip address: '+socket.inet_ntoa(ip_hdr[1])
	print '[*]Destination ip address: '+socket.inet_ntoa(ip_hdr[2])
	print '[*]Source Port : ' + str(source_port)
	print '[*]Dest Port : ' + str(dest_port) 
	print '[*]Sequence Number : ' + str(sequence)  
	print '[*]Acknowledgement : ' + str(acknowledgement)  
	print '[*]TCP header length : ' + str(tcph_length)
	print '[*]DATA : ' + str(data)

