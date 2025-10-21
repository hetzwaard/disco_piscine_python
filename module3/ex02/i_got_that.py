#!/usr/bin/env python3
STOP = "STOP"

question = input("What you gotta say? : ")

if question == STOP:
	exit(0)

i = 1
while i > 0:
	loop = input("I got that! Anything else? : ")
	if loop == STOP:
		exit(0)