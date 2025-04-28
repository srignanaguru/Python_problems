from collections import defaultdict
def groupanagrams(strs):
    group_anagram=defaultdict(list)
    for word in strs:
        sorted_anagram="".join(sorted(word))
        group_anagram[sorted_anagram].append(word)
    return list(group_anagram.values())

    

strs=["eat","tea","tan","ate","nat","bat"]
res=groupanagrams(strs)
print(res)