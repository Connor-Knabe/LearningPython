fiz = "fizzbuzzb"

#f = -1

f = fiz.find("f")
b = fiz.rfind("b")

if f == 0:
	print "fizz"
if b == len(fiz)-1:
	print "buzz"
if f == 0 and b == len(fiz)-1:
	print "fizzbuzz"