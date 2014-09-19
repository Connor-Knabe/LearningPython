import os
outFile = open('./Grades.txt', 'w+')
pwprtName = ""
pwprtArry = []

#Loops through all files changing the name to pwprt.php
#Also adds the pwprt to an array
for filename in os.listdir("."):
	if filename.startswith("Lab ") and "php" in filename:
		pwprtName = filename.split('_')[1]+".php"
		os.rename(filename, pwprtName)
		pwprtArry.append(pwprtName.split(".")[0])

#Sorts array and prints to Grades file
pwprtArry.sort()
for j in range (len(pwprtArry)):
    outFile.write(pwprtArry[j] + " -" + "\n")