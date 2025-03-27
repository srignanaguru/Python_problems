def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return i,j
nums=[2,4,5]
target=7
res=twoSum(nums,target)
print(f"Target no. indicies:{res}")
