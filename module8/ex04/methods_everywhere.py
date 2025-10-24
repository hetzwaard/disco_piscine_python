#!/usr/bin/env python3

import sys

def shrink(s):
	print(s[0:8])
	
def enlarge(s):
	print(s[0:len(s)], end="")
	i = len(s)
	while 8 > i:
		print("Z", end="")
		i += 1
	print("")

if len(sys.argv) < 2:
	print("none")
else:
	i = 1
	while len(sys.argv) > i:
		if len(sys.argv[i]) > 8:
			shrink(sys.argv[i])
		elif len(sys.argv[i]) < 8:
			enlarge(sys.argv[i])
		else:
			print(sys.argv[i])
		i += 1
