#arr = [0,1,2,3,4,22]

def helper(sol_arr, arr, i):
	#print "length=", len(arr), "\n"

	#print "Index", i, arr[i]
	arr[i] *= 2

	#print "Index after", i, arr[i]
	i += 1


	if i < len(arr):

		#print "Got into if && index = ", i
		return helper(sol_arr,arr,i)
	else:
		#print "Returning from if", i
		return arr

def times2(arr):
	print arr
	sol_arr = []

	solution_arr = helper(sol_arr, arr, 0)
	print solution_arr
	return solution_arr

#times2(arr)