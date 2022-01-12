def sum_index_multiplier(nums):
	return sum(j*i for i, j in enumerate(nums))

print(sum_index_multiplier([1,2,3,4]))
print(sum_index_multiplier([-1,-2,-3,-4]))
print(sum_index_multiplier([]))
