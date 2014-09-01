string = "Code"
finalString = ""

for i in range(0,len(string)):
	if i == 0:
		finalString += string[0]
		finalString += string[0]
	elif i == 1:
		finalString += string[1]
	elif i == 2:
		finalString += string[0:3]
	elif i == 3:
		finalString += string[0:4]

print finalString

finalString += string[0:1] #first letter
finalString += string[0:1] #first letter

finalString += string[1:2] #second letter

finalString += string[0:3] #third letter

finalString += string [0:4] #fourth letter
