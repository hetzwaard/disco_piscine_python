#!/usr/bin/env python3

import sys

def greetings(s=None):
	if s is None:
		s = "noble stranger"
	else:
		if not isinstance(s, str):
			print("Error! It was not a name")
			exit (1)
	print("Hello, " + s + ".")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
