def near_hundred(n):
	if (n < 111) and abs(n-100 < 11):
		return True
	elif (n > 111) and abs(n-200 < 11):
		return True
	else:
		return False
