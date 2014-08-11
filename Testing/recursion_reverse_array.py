arr = [1,2,3]

def helper(arr,i,k,rev_arr):
	arr_size_index = len(arr)-1
	print "i is ",i
	print "k is ",k

	for d in range (len(rev_arr)):
		print rev_arr[d] 

	rev_arr[k] = arr[i]
	print "AFTER"
	for d in range (len(rev_arr)):
		print rev_arr[d] 
	i -= 1
	k += 1

	if k > len(rev_arr):
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
	rev_arr = arr
	sol_arr = []

	sol_arr = helper(arr,len(arr)-1,0,rev_arr)

	#print sol_arr[0]

	#for i in range (len(sol_arr)):
	#	print sol_arr[i]

	
reverse(arr)