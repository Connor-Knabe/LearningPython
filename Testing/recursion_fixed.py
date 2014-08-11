arr = [0,1,2,3,4,22]
def helper(sol_arr, arr, i):
	arr[i] *= 2
	print arr[i]
	i += 1

	if i < len(arr):
		helper(sol_arr,arr,i)
	else:
		return arr

def times2(arr):
	sol_arr = []
	solution_arr = helper(sol_arr, arr, 0)
	return solution_arr

times2(arr)