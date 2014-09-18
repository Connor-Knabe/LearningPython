import os
str = ""
arr = []
i = 0
for filenames in os.listdir('.'):
    str = filenames.split(".")[0]
    arr.append(str)
    i += 1

arr.sort()
for j in range (len(arr)):
    print arr[j],"-","\n"
