str = "hixxhi"
firstSubStr = ""
secondSubStr = ""
j = 0
for i in range (len(str)):
	firstSubStr = str[i:i+2]
	for k in range (len(str)):
		secondSubStr = str[k+1:k+3]
		if firstSubStr == secondSubStr:
			j += 1
		print "first",firstSubStr, "second", secondSubStr

print j