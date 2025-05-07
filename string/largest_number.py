from functools import cmp_to_key

def compare(a, b):
    if a+b>b+a:
        return -1
    elif a+b<b+a:
        return 1
    else:
        return 0


def largestnum(nums):
    nums=list(map(str, nums))
    nums.sort(key=cmp_to_key(compare))
    res=''.join(nums)
    return '0' if res[0]=='0' else res
nums = [10,2,9]
res=largestnum(nums)
print(res)