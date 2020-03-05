from collections import defaultdict, Counter

def myFun(S):
    p = ''.join(set(S))
    cou = Counter(p) 
    rq = len(cou)
    l = 0
    r = 0
    u = 0
    ud = {}
    mwl = float("inf")
    wl = None
    wl = None
    while r < len(S):
        ud[S[r]] = ud.get(S[r], 0) + 1
        if S[r] in cou and ud[S[r]] == cou[S[r]]:
            u += 1
        while l <= r and u == rq:
            if r - l + 1 < mwl:
                mwl = r - l + 1
                wl = l
                wl = r
            ud[S[l]] -= 1
            if S[l] in cou and ud[S[l]] < cou[S[l]]:
                u -= 1
            l += 1
        r += 1
    return "" if mwl == float("inf") else len(S[wl: wl + 1])

S = input()
result = myFun(S)
print (result)
