import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbosity", help="increase output verbosity")
parser.add_argument("--quit", help="quit mode")
args = parser.parse_args()
if args.verbosity:
    print "verbosity turned on"
if args.quit:
	print "quit turned on!!!!"