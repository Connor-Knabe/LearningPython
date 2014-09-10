n = 9

def fib(n):
	if (n<2):
		print "YES"
		return n
	else:
		return (fib(n-1)+(fib(n-2)))

print fib(n);