#Given the array arr as input, return the array with each item in the array multiplied by two

#Run with: python test.py one



def times2(arr):
	for i in range (0, len(arr)):
		arr[i] *= 2
	return arr