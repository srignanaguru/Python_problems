import re
def isvalidpalindrome(s):
    s=s.replace(" ","")
    s=re.sub(r'[^a-zA-Z]','',s)
    s=s.lower()
    n=len(s)
    reverses=s[::-1]
    if s==reverses:
        return True
    else:
        return False

s="A man, a plan, a canal: Panama"
res=isvalidpalindrome(s)
print(res)
