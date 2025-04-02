def majority_element(nums):
    n=len(nums)
    appear=n/2
    count_num={}
    for num in nums:
        if num in count_num:
            count_num[num]+=1
        else:
            count_num[num]=1
    for key, value in count_num.items():
        if value>=appear:
            return key


num=[3,2,3]
res=majority_element(num)
print(res)