#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import struct

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW)
s.bind(('eth0',0x800))

# ETHERNET
dst_host = '\xff\xff\xff\xff\xff\xff'
src_host = '\x00\x26\xc6\x8f\x22\x64'
eth_type = '\x08\x06'
# ARP
hw_type = '\x00\x01'
proto_type = '\x08\x00'
hw_add_len = '\x06'
proto_add_len = '\x04'
opcode = '\x00\x01'
src_hw_add = '\x00\x26\xc6\x8f\x22\x64'
src_proto_add = '\xC0\xA8\x01\x65'
dst_hw_add = '\xff\xff\xff\xff\xff\xff'
dst_proto_add = '\xC0\xA8\x01\x33'

arp = struct.pack("!6s6s2s2s2s1s1s2s6s4s6s4s",    dst_host,src_host,eth_type,hw_type,proto_type,hw_add_len,proto_add_len,opcode,src_hw_add,src_proto_add,dst_hw_add,dst_proto_add)

s.send(arp)