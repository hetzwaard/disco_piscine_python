#!/usr/bin/env python3

def array_of_names(dic):
	return [f"{k.capitalize()} {v.capitalize()}" for k, v in dic.items()]

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(persons))
