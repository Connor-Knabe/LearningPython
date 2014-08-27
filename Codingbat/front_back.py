str = "aa"

if len(str) == 2:
	first = str [:1]
	last = str[1:]
	print "last first",last + first

first = str[0:1]
last = str[len(str)-1:]
middle = str[1:len(str)-1]
print last + middle + first


