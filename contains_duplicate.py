def is_duplicate(nums):
    con={}
    for num in nums:
        con[num]=con.get(num,0)+1
    for key, value in con.items():
        if value>1:
            return True
    return False
nums=[2,14,18,22,22]
res=is_duplicate(nums)
print(res)