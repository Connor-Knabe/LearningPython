string = "kitten"
n = 4

firstStr = ""
lastStr = ""

if (n==0):
	print "first letter",string[n+1:]
elif (n==len(string)-1):
	print "last letter",string[0:len(string)-1]
else:
	firstStr = string[0:n]
	lastStr = string[n+1:len(string)]
	print "Final",firstStr + lastStr



print string[len(string)-1]