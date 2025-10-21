#!/usr/bin/env python3
number = input("Enter a number\n")
number = int(number)

i = 0
while i <= 9:
	print(i, "x", number, "=", number * i)
	i += 1
