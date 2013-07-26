#!/usr/bin/env python
import sys
from scapy.all import *

while True:
	sr(IP(dst=sys.argv[1])/UDP()/fuzz(DNS()),inter=1,timeout=1)