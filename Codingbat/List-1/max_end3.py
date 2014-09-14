nums = [1,2,3]
max = 0
for i in range (len(nums)):
	if (nums[i] > max):
		max = nums[i]

for i in range (len(nums)):
	nums[i]=max

print nums

