fiz = "fizzbuzzb"

f = -1

#f = fiz.rfind(f)

f = fiz.find("f")
b = fiz.rfind("b")

count = fiz.count("z")

print fiz, "count is ", count

print "Was f found?", f


if f == 0:
	print "fizz"
if b == len(fiz)-1:
	print "buzz"
if f == 0 and b == len(fiz)-1:
	print "fizzbuzz"