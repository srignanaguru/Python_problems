from collections import Counter

def anagramindex(text, pattern):
    result=[]
    pattern_count=Counter(pattern)
    window_count=Counter()
    window_size=len(pattern)
    for i in range(len(text)):
        window_count[text[i]]+=1

        if i>=window_size:
            if window_count[text[i - window_size]]==1:
                del window_count[text[i-window_size]]
            else:
                window_count[text[i - window_size]]-=1
        if window_count==pattern_count:
            result.append(i - window_size+1)
    return result

text = "cbaebabacd"
pattern = "abc"

res=anagramindex(text,pattern)
print(res)