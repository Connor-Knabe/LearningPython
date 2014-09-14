nums = [2,3]
sum=0
if len(nums)<2:
    sum = 0 if len(nums)==0 else nums[0]
else:
	sum = nums[0] + nums[1]
print sum