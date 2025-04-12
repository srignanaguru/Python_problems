def movetoend(nums):
    res=[x for x in nums if x!=0] + [x for x in nums if x==0] 
    return res

nums=[0,1,0,3,12]
res=movetoend(nums)
print(res)