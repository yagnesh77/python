def elements_difference(nums):
    result = [j-i for i, j in zip(nums[:-1], nums[1:])]
    return result

nums1 = [1,2,3,4,5,6,7,8,9,10]
nums2 = [2,4,6,8]

print("Original list:")
print(nums1)
print(elements_difference(nums1))
print("\nOriginal list:")
print(nums2)
print(elements_difference(nums2))

