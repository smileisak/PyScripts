#!/usr/bin/env python


import signal

def ctrlc_handler(signum,frm):
	print "HAHAHAHA! you cannot kill me!"
	print "ok only for this time ! "
	exit()

print "Installing signal handler ...."
signal.signal(signal.SIGINT , ctrlc_handler)

print "done!"


while True:
	pass