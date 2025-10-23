#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
	print("none")
else:
	parameter = sys.argv[1]
	check = input("What was the parameter? ")
	if check == parameter:
		print("Good job!")
		exit (0)
	else:
		print("Nope, sorry...")
		exit(0)
