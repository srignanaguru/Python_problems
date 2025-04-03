def sort_colors(nums):
    count_nums1=count_nums2=count_nums0=0
    for num in nums:
        if num==0:
            count_nums0 +=1
        elif num==1:
            count_nums1 += 1
        elif num==2:
            count_nums2 += 1

    index=0
    for _ in range(count_nums0):
        nums[index]=0
        index+=1
    for _ in range(count_nums1):
        nums[index]=1
        index+=1
    for _ in range(count_nums2):
        nums[index]=2
        index+=1
    return nums
nums=[2,0,2,1,1,0]
res=sort_colors(nums)
print(res)