nums = [1,2,3]

nums[2,3,1]


    temp0 = nums[0]
    temp1 = nums[1]
    temp2 = nums[2]

    nums[0] = temp1
    nums[1] = temp2
    nums[2] = temp0

    return nums
