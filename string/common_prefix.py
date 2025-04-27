def commonprefix(strs):
    if not strs:
        return ""
    
    prefix = ""
    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return prefix
        prefix += char
    return prefix
        
strs = ["flower","flow","flight"]
res=commonprefix(strs)
print(res)