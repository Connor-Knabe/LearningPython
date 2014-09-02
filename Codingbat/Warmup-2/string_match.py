string1 = "abc"
string2 = "abc"

for i in range (len(string1)):
	if string1[i:i+2] == string2[i:i+2]:
		print "YE"