#!/usr/bin/env python3
arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = [x + 2 for x in arr1 if x > 5]

arr2 = list(dict.fromkeys(arr2))

print("Original array:", arr1)
print("New array:", arr2)
