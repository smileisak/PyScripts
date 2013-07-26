#!/usr/bin/env python

import os
def child_process ():
	print "i'm the child process and my PID is : %d"%os.getpid()
	print "the child is exiting"

def parent_process():
	print "i'm the parent process with PID %d"%os.getpid()
	childpid = os.fork()
	if childpid == 0 :
		#we are inside the child
		child_process()
	else :
		#we are inside the parent process
		print "We are inside the parent process"
		print "Our child has PID : %d"%childpid
	
	while True :
		pass

parent_process()

