str = "Heeololeo"

finalStr = ""


for i in range (0,len(str)):
	if i % 2 == 0:
		finalStr += str[i]

print finalStr