def calculate(s):
    stack=[] # Initializing stack
    num=0 # To parse the current integer
    res=0 # To store the result
    sign=1 # To identify is this +ve or -ve

    for c in s:
        if c.isdigit():
            num=num*10+int(c) # parsing the integer #19
        elif c in "+-":
            res+=sign*num #1
            num=0
            if c=='+': # Checking whether the c sign
                sign=1
            else:
                sign=-1
        elif c in '(':
            stack.append(num) #0
            stack.append(sign) #1
            res=0
            sign=1
        elif c in ')':
            res+=sign*num #1=1+1*9=10
            num=0
            res*=stack.pop() # Assinging Sign  
            res+=stack.pop() # Summation of Integer
    res+=sign*num
    return res

s="(1+9)"
res=calculate(s)
print(res)