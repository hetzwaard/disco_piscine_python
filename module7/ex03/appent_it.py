#!/usr/bin/env python3
import sys
import re

if len(sys.argv) < 2:
	print("none")
	exit (0)
else:
	i = 1
	while len(sys.argv) > i:
		flag = sys.argv[i].find("ism", len(sys.argv[i]) - 3, len(sys.argv[i]))
		if flag == -1:
			print(sys.argv[i] + str("ism"))
		i += 1
