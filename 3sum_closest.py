def threesum(nums, target):
    arrsort=sorted(nums)
    diff=[]
    for i in range(len(nums)):
        val=abs(nums[i]-target)
        diff.append([nums[i],val])
    sorted(diff)
    closet=[]
    for pair in diff:
        closet.append(pair[0])
    sumval=0
    for x in closet[0:3]:
        sumval+=x
    return sumval

nums=[-1,2,1,4]
Target=1
res=threesum(nums,Target)
print(res)