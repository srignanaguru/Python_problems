def consecutive(nums):
    if not nums:
        return 0
    arr=set(nums)
    sort_arr=sorted(arr)

    max_streak=1
    current_streak=1

    for i in range(1,len(sort_arr)):
        if sort_arr[i] - sort_arr[i-1]==1:
            current_streak+=1
        else:
            max_streak=max(max_streak, current_streak)
            current_streak=1
    max_streak=max(max_streak, current_streak)
    return max_streak
    


nums=[100,4,200,1,3,2]
res=consecutive(nums)
print(res)