def checkparen(s):
    stack=[]
    dic={')':'(',']':'[','}':'{'}

    for c in s:
        if c in dic.values():
            stack.append(c)
        elif c in dic:
            if not stack or stack[-1]!=dic[c]:
                return False
            stack.pop()
    
    return True


s="()[]}"
res=checkparen(s)
print(res)