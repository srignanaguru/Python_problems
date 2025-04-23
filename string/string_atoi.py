def stringatoi(s):
    s = s.lstrip() 
    if not s:
        return 0

    sign, i, n = 1, 0, len(s)
    if s[0] in "+-":
        if s[0] == '-':
            sign = -1
        i += 1

    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1

    num *= sign
    return max(-2**31, min(num, 2**31 - 1))

s=" 42"
res=stringatoi(s)
print(res)