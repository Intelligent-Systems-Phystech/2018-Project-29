#!/usr/bin/env python
import subprocess
import argparse
import sys

#command line argument parser. What else arguments do we need?
def createParser ():
	parser = argparse.ArgumentParser()
	parser.add_argument('--epochs', nargs='?', default='5')
	return parser

if __name__ == '__main__':
	parser = createParser()
	args = parser.parse_args(sys.argv[1:])
	for i in range(args.epochs):
		##here we do smth

