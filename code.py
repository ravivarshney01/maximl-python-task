from collections import defaultdict, Counter

def myFun(stri):
    p = ''.join(set(stri))
    cou = Counter(p) 
    rq = len(cou)
    l = 0
    r = 0
    u = 0
    ud = {}
    mwl = float("inf")
    wl = None
    wl = None
    while r < len(stri):
        ud[stri[r]] = ud.get(stri[r], 0) + 1
        if stri[r] in cou and ud[stri[r]] == cou[stri[r]]:
            u += 1
        while l <= r and u == rq:
            if r - l + 1 < mwl:
                mwl = r - l + 1
                wl = l
                wl = r
            ud[stri[l]] -= 1
            if stri[l] in cou and ud[stri[l]] < cou[stri[l]]:
                u -= 1
            l += 1
        r += 1
    return "" if mwl == float("inf") else len(stri[wl: wl + 1])

stri = input()
result = myFun(stri)
print (result)
