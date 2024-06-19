#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

nums = [1,1,2]
k = len(nums) 
print(k)


j=1
for i in range(1,k):
    
    if(nums[i] != nums[i-1]):
        nums[j] = nums[i]
        j+=1



print(j)
print(nums)
