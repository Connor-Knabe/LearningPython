str = "abcxyz"

for i in range (len(str)):
	if str[i:i+3] == "xyz":
		print "YES"
