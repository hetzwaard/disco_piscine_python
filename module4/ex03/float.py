#!/usr/bin/env python3
number = input("Give me a number: ").strip()

result = float(number)
if result.is_integer():
	print("This number is an integer.")
else:
	print("This number is a decimal.")
