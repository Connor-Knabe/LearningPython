#Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum. 

a = 3
b = 2
c = 3
sum = 0

if (a != b and a != c):
	sum +=a
if (b != a and b != c):
	sum +=b
if (c != a and c != a):
	sum +=c
