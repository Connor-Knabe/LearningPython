string = "Kitten"
finalString = ""



for i in range (len(string)):
	if i == 0 and len(string) > 0:
		finalString += string[0]
		finalString += string[0]
	elif i == 1:
		finalString += string[1]
	elif i == 2:
		finalString += string[0:3]
	elif i > 2 and len(string)-1 != i: 
		print "HE"
		finalString += string[0:i+1]
	elif i == len(string)-1:
		print "HI"
		finalString += string


print finalString

