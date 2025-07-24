def checkparen(s):
    stack=[]
    dic={')':'(',']':'[','}':'{'}

    for c in s:
        if c in dic.values(): 
            stack.append(c)
        elif c in dic:
            if not stack or stack[-1]!=dic[c]: # Checking whether the stack is empty or current char is not equal to the dic of key & value pair
                return False
            stack.pop()
        else:
            return False
    
    return True


s="()[]}"
res=checkparen(s)
print(res)
