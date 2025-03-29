def three_sum(nums):
    merged=[]
    sort=[]
    res=[]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if (i!=j and j!=k and k!=i) and (nums[i] + nums[j] + nums[k]==0):
                    merged.append([nums[i],nums[j],nums[k]])
    for mer in merged:
        sort.append(sorted(mer))
    for dup in sort:
        if dup not in res:
            res.append(dup)
    return res
nums = [-1,0,1,2,-1,-4]
res=three_sum(nums)
print(res)
#[[-10,5,5],[-5,0,5],[-4,2,2],[-3,-2,5],[-3,1,2],[-2,0,2]]