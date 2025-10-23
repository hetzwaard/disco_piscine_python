#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 2:
	print("none", end="")
else:
	s1 = str("z")
	res = len(re.findall(s1, sys.argv[1]))
	if res == 0:
		print("none", end="")
	while res > 0:
		print("z", end="")
		res -= 1
print("")
