#! /usr/bin/env python3
'''
A beautiful and and fast algorithm to solve this problem is implemented here
'''

def pal_check(n):
	num = str(n)
	if (num == num[::-1]):
		return True
	else:
		return False

largest_pal = 0
a = 999
while (a >= 100): # As we know that any palindrome will have 11 as one of the factors
	if (a % 11 == 0):
		b = 999
		db = 1
	else:
		b = 990 # last 3-digit number divisible by 11
		db = 11
	while (b >= a):
		if (a * b < largest_pal):
			break
		if pal_check(a * b):
			largest_pal = a * b
		b = b - db
	a = a - 1

print(largest_pal)
