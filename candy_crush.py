def candy_crush(S, k):
    stack = []
    stack.append([S[0],1])
    for i in S[1:]:
        if stack and stack[-1][0] == i:
            stack[-1][1] += 1
        else:
            if stack and stack[-1][1] >= k:
                stack.pop()
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i,1])
    if stack and stack[-1][1] >= k:
        stack.pop()
    return ''.join([i[0]*i[1] for i in stack])
            
from functools import lru_cache
from itertools import groupby
@lru_cache()
def candyCrush1D_followup(S):
    l, segs = 0, []
    for c, seq in groupby(S):
        k = len(list(seq))
        if k >= 3:
            segs.append((l, l + k))
        l += k
    return min([
        candyCrush1D_followup(S[:l] + S[r:]) 
        for l, r in segs
    ], key=len, default=S)
        

assert candy_crush("aaabbbc", 3) == "c"
assert candy_crush("aabbbacd", 3) == "cd"
assert candy_crush("baaabbbabbccccd", 3) == "abbd"
assert candy_crush("bbbbbbb", 3) == ""
assert candy_crush("aaabbbacd", 3) == "acd"
assert candy_crush("ccddccdcaacabbbaaccaccddcdcddd", 3) == ""

