from collections import Counter
def longestpalindrome(s):
    count=Counter(s)
    half=[]
    middle=""
    for char, freq in sorted(count.items()):
        if freq%2==1:
            middle=char
        half.append(char*(freq//2))
    half_str="".join(half)
    return len(half_str+middle+half_str[::-1])

s="abccccdd"
res=longestpalindrome(s)
print(res)