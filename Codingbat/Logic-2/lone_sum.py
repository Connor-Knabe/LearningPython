#Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum. 

a = 2
b = 2
c = 2
sum = 0
    if (a != b and a != c):
        sum = a+b
    if (b != c):
    	sum += b+c
print sum
