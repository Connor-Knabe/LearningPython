#Given a number n, return True if n is in the range 1..10, inclusive. Unless "outsideMode" is True, in which case return True if the number is less or equal to 1, or greater or equal to 10. 

n = 1
outside_mode = True

if (n >= 1 and n <= 10 and not outside_mode):
	print "TRUE"