
def helper(arr,i,rev_arr):
	#print "i is ",i
	#print "k is ",k

	#print "rev_arr[k] = ", rev_arr[k]
	#print "arr[i] = ", arr[i]

	#print "\nArry[0]", arr[0]

	rev_arr.append(arr[i])

	#k += 1

	#if k >= len(rev_arr):
	#	print "DONE"
	#	#for d in range (len(rev_arr)):
	#	#	print rev_arr[d] 
	#	return rev_arr
	#else:
	#	return helper(arr,i,k,rev_arr)

	if i == 0:
		return rev_arr
	else:
		i -= 1

		return helper(arr,i,rev_arr)


def reverse(arr):
	#Your code goes here and remember you can add other methods to help out if you like.
	
	arr2 = [1,2,3,4,5,6,7,8]

	#sol_arr = []

	sol_arr = helper(arr2,len(arr2)-1,[])

	print sol_arr

	#print sol_arr[0]

	#for i in range (len(sol_arr)):
	#	print sol_arr[i]

	
reverse([])