string = "There"
finalString = ""



for i in range(0,len(string)):
	if i == 0:
		finalString += string[0]
		finalString += string[0]
	elif i == 1 and len(string) > 1:
		finalString += string[1]
	elif i == 2 and len(string) > 2:
		finalString += string[0:3]
	elif i == 3 and len(string) > 3:
		finalString += string[0:4]
	elif i == 4 and len(string) > 4:
		finalString += string[0:len(string)-1]
	elif i == len(string)-2:
		finalString += string





print finalString

