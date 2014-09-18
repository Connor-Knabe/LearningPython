import os
arr = []
outFile = open('./names.txt', 'w+')
i = 0
for filenames in os.listdir('.'):
    arr.append(filenames.split(".")[0])
    i += 1

arr.sort()
for j in range (len(arr)):
    outFile.write(arr[j] + "-" + "\n")
