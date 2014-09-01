string = "ab"

finalString = ""

finalString += string[:1]
finalString += string[:1]

finalString += string[1:2]
finalString += string[:1]
finalString += string[1:2]
finalString += string[2:3]
finalString += string[0:len(string)]

print finalString