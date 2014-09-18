import os
outFile = open('./cs3380Grades.txt', 'w+')
pwprtName = ""
pwprtArry = ""
for filename in os.listdir("."):
	if filename.startswith("Lab "):
		pwprtName = filename.split('_')[1]+".php"
		os.rename(filename, pwprtName)
		pwprtArry.append(pwprtName.split(".")[0])

pwprtArry.sort()
for j in range (len(arr)):
    outFile.write(arr[j] + " -" + "\n")