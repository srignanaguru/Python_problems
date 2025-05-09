def is_palindrome(word):
    return word==word[::-1]

def palindrome_pairs(words):
    word_map={word: i for i, word in enumerate(words)}
    res=[]

    for i, word in enumerate(words):
        for j in range(len(word)+1):
            prefix=word[:j]
            suffix=word[j:]

            if is_palindrome(prefix):
                reversed_suffix=suffix[::-1]
                if reversed_suffix in word_map and word_map[reversed_suffix]!=i:
                    res.append([word_map[reversed_suffix], i])
                if j!=len(word) and is_palindrome(suffix):
                    reversed_prefix=prefix[::-1]
                    if reversed_prefix in word_map and word_map[reversed_prefix]!=i:
                        res.append([i, word_map[reversed_prefix]])
    return res
        
strs=["bat","tab","cat"]
res=palindrome_pairs(strs)
print(res)