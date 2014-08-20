#FIBONACCI MOTHER FUCKER
#If you aren't already familiar, the Fibonacci Sequence is an infinite sequence of numbers
#where the nth number is equal to (n-1)+(n-2)
#n = (n-1)+(n-1)
#For example the first number is 0, the second number is 1, these first two values are given and then the sequence is started.
#The sequence looks like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#Given an integer n as input, return the nth Fibonacci number. For example given 6, your function should return 8 or given 8 your 
#function should return 21
#Your solution MUST be recursive. NO LOOPS ALOUD 
#NOTE: I STARTED THE COUNT FROM ZERO SO THE ZEROTH FIBONACCI NUMBER IS ZERP AND THE FIRST IS ONE AND THE SECOND IS ONE AND THE THIRD IS TWO AND SO ON

#fibonacci(8) -> 21
#fibonacci(6) -> 8

def fibnocci(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fibnocci(n-1)+fibnocci(n-2)



def fibonacci(n):
	#Your code goes here. Remember a helper function is a good idea
	x = fibnocci(8)
	print x
	return x
