print "Hi there"

i = -1

if i > 0:
	print "I greather than zero"
else:
	print i ,"Is less than zero"


for i in range(0,10):
	print i

arry = [0,1,2,3,4]

#for i in range(0,len(arry))
print "Array index 4", arry[4]


print "Arry length = ", len(arry)


def tttt(arry):
	for i in arry[:]:
		print "Array",i
		
tttt(arry)

