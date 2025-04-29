from collections import defaultdict
def longestrepeatingchar(s,k):
    count=defaultdict(int)
    max_freq=0
    left=0
    result=0

    for right in range(len(s)):
        count[s[right]]+=1
        max_freq=max(max_freq, count[s[right]])

        while (right - left +1) -max_freq>k:
            count[s[left]]-=1
            left+=1
        result=max(result, right-left+1)
    return result


s="AABABBA"
k=1
res=longestrepeatingchar(s,k)
print(res)