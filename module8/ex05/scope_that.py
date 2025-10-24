#!/usr/bin/env python3

def add_one(value):
	value += 1
	print("inside add_one: value =", value)


def main():
	number = 5
	print("before calling add_one: number =", number)
	add_one(number)
	print("after calling add_one: number =", number)

main()
