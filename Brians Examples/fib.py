n = 5

def fib(n):
	if (n<2):
		return n
	else:
		return (fib(n-1)+(fib(n-1)))

print fib(n);