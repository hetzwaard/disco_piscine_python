#!/usr/bin/env python3

import sys

def downcase_it(s):
	return s.lower()

if len(sys.argv) < 2:
	print("none")
	exit(0)
else:
	i = 1
	while len(sys.argv) > i:
		print(downcase_it(sys.argv[i]))
		i += 1