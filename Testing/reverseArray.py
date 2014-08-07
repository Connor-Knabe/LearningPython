array = [5,10,15,20]
#array2 = [1,2,3,4]


for i in range (0, len(array)):
	print "Array normal: ", array[i]

array.reverse()

for i in range (0, len(array)):
	print "Array reversed: ", array[i]

print "How many 5s in array:", array.count(5)