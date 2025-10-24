#!/usr/bin/env python3

def find_the_redheads(dic):
	return list(filter(lambda k: dic[k] == "red", dic.keys()))

dupont_family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
}

print(find_the_redheads(dupont_family))
