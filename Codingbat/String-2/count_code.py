str = "aaacodxbbb"
finalStr = ""
for i in range (len(str)):
	finalStr = str[i:i+4]
	if finalStr[:2] == "co":
		print "YES"
	if finalStr[3:] == "e":
		print "YES"
	print finalStr
	#if str[i:i+4] == "code":
		#print "YES"