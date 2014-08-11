arr = [1,2,3,4,5,6,7,8]

def helper(arr,i,k,rev_arr):
	arr_size_index = len(arr)-1
	print "i is ",i
	print "k is ",k

	print "rev_arr[k] = ", rev_arr[k]
	print "arr[i] = ", arr[i]

	print "\nArry[0]", arr[0]

	rev_arr[k] = arr[i]

	i -= 1
	k += 1

	if k >= len(rev_arr):
		print "DONE"
		for d in range (len(rev_arr)):
			print rev_arr[d] 
		return rev_arr
	else:
		helper(arr,i,k,rev_arr)

	#if k < len(rev_arr):
	#	helper(arr,i,k,rev_arr)
	#else:
	#	print "DONE"
	#	for d in range (len(rev_arr)):
	#		print rev_arr[d] 
	#	return rev_arr

def reverse(arr):
	#Your code goes here and remember you can add other methods to help out if you like.
	rev_arr = array.copy(arr)

	sol_arr = []

	sol_arr = helper(arr,len(arr)-1,0,rev_arr)

	#print sol_arr[0]

	#for i in range (len(sol_arr)):
	#	print sol_arr[i]

	
reverse(arr)