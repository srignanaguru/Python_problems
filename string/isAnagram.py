from collections import Counter

def isAnagram(s, t):
    if(len(s)!=len(t)):
        return False
    return Counter(s)==Counter(t)


s="anagram"
t="nagaram"
res=isAnagram(s,t)
print(res)