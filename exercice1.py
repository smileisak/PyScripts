#!/usr/bin/env python

dmesg = open("/var/log/dmesg" , "r")
for line in dmesg:
	if "USB " in line:
		print line




