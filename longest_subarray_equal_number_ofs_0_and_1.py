def longest_length(nums):
    for i in range(len(nums)):
        if nums[i]==0:
            nums[i]=-1
    prefix={}
    prefix_sum=0
    max_len=0
    for i in range(len(nums)):
        prefix_sum+=nums[i]
        if prefix_sum==0:
            max_len=i+1
        elif prefix_sum not in prefix:
            prefix[prefix_sum]=i
        elif prefix_sum in prefix:
            dist=i-prefix[prefix_sum]
            max_len=max(dist, max_len)
    return max_len

nums=[0,1]
res=longest_length(nums)
print(res)