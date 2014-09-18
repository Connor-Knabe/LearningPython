import os
str = ""
out1 = "" 
arr = []
outFile = open('./testfile', 'w+')
i = 0
for filenames in os.listdir('.'):
    str = filenames.split(".")[0]
    arr.append(str)
    i += 1

arr.sort()
for j in range (len(arr)):
    out = arr[j] + "-" + "\n"
    outFile.write(out)
    print 
