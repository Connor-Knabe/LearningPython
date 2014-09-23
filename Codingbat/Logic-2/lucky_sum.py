#Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count. 

sum=0
a=2
b=2
c=2

if a != b and a != c: sum += a
if a == 13: print sum
if b != a and b != c: sum += b
if b == 13: print sum
if c != a and c != b: sum += c
if c == 13: print sum


print sum