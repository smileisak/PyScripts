#!/usr/bin/env python

import os 
import sys
import time


for root, dirnames, filenames in os.walk(sys.argv[1]):
	#print list(dirnames)
	
		for d in dirnames:
				print "***" + d
				for f in filenames:   
					print "-------"+ f 
					print "\n size====>"+ str(os.stat(os.path.join(root, f)).st_size)
					print "\n uid====>"+ str(os.stat(os.path.join(root, f)).st_uid)
					print "\n recent access time ====>"+ str(os.stat(os.path.join(root, f)).st_atime/100)





					







