#!/usr/bin/env python3
number = input("Enter a number less than 25\n")

if int(number) >= 25:
	print("Error")
else:
	number = int(number)
	while number <= 25:
		print("Inside the loop, my variable is", number)
		number += 1
		