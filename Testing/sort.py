array = [1,2,33,2,3,4,1,3]

for i in range (0,len(array)):
	print "i=", array[i]

array.sort()

for i in range (0,len(array)):
	print "Sorted array i=", array[i]

array.reverse()

print ""

for i in range (0,len(array)):
	print "Reversed array i=", array[i]