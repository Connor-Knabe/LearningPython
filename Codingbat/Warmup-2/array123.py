def array123(nums):
  
    one = 0
    two = 0
    three = 0

    for i in range (0,len(nums)):
        if nums[i] == 1:
	    one += 1
	elif nums[i] == 2:
	    two += 1
	elif nums[i] == 3:
	    three += 1
    if one >= 1 and two >= 1 and three >= 1:
        return True
    else:
        return False