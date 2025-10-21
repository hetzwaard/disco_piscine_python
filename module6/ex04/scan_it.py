#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
	print("none")
else:
	s1 = str(sys.argv[1])
	s2 = str(sys.argv[2])
	res = len(re.findall(s1, s2))
	if res == 0:
		print("none")
		exit (0)
	print(res)
