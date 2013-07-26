#/usr/bin/python


def print5times(line_to_print):
	for count in xrange(0,5):
		print line_to_print


print5times(sys.args[0])

