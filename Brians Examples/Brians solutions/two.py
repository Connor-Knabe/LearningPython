#Given the array arr as input return that array reverse
#Example: Given [1, 2, 3, 4] return [4, 3, 2, 1]

#Run with: python test.py two

def reverse(arr):
    #Your code goes here
	i = len(arr)
	sol = []
	for element in arr:
		sol.append(arr[i-1])
		i -= 1
	return sol
