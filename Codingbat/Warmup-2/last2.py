str = "axxxaaxx"
lastSubString = ""
compSubString = ""

lastSubString = str[len(str)-2:len(str)]

for i in range (len(str)):
	compSubString = str[i:i+2]

	print "len str", len(str), "i=",i

	if compSubString == lastSubString and len(str)-2 != i:
		print "YES", compSubString

print lastSubString