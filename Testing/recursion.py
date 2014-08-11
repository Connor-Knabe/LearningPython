arr = [0,1,1,3,4]

def helper(sol_arr, arr, i):
#Your code goes here
    arr[i] *= 2
	i += 1
    helper(sol_arr, arr,i)
    if  i+1 == len(arr):
    	print i

def times2(arr):
    sol_arr = []
    solution_arr = helper(sol_arr, arr, 0)
    return solution_arr

times2(arr)