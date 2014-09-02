str = "hixxhi"
firstSubStr = ""
for i in range (len(str)):
	if str[i:i+1] == str[i+1:i+2]:
		print "true"
