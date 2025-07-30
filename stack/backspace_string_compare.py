def bckstrcmp(s, t):
    stk1=[]
    stk2=[]

    for c in s:
        if c!='#':
            stk1.append(c)
        else:
            if stk1:
                stk1.pop()
    
    for c in t:
        if c!='#':
            stk2.append(c)
        else:
            if stk2:
                stk2.pop()
    return True if len(stk1)==len(stk2) and stk1==stk2 else False
    
    

s="a#c"
t="b"
res=bckstrcmp(s, t)
print(res)