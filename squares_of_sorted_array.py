def squaresarr(nums):
    res=[]
    for i in range(len(nums)):
        val=nums[i]**2
        res.append(val)
    return sorted(res)

nums=[-4,-1,0,3,10]
res=squaresarr(nums)
print(res)