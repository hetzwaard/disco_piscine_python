#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
	print("none")
	exit (0)
else:
	n1 = int(sys.argv[1])
	n2 = int(sys.argv[2])
	arr = list(range(n1, n2+1))
	print(arr)
