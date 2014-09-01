nums = [1,2,1,1,9,4,1,9]

print len(nums)
k = 0



for i in range (0,len(nums)):
	if nums[i] == 9 and k <= 4:
		print "true"
	k += 1
print "false"
