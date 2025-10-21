#!/usr/bin/env python3
first_number = input("Enter the first number:\n")
second_number = input("Enter the second number:\n")

result = int(first_number) * int(second_number)

print(first_number, "x", second_number, "=", result)

if int(result) == 0:
	print("The result is positive and negative.\n")
elif int(result) < 0:
	print("The result is negative.\n")
else:
	print("The result is positive.\n")
