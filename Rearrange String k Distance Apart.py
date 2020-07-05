import collections
def rearrangeString(strs, k):
    if (k == 0):
        return strs
    res = []
    size = len(strs)
    
    q = []
    m = collections.Counter(strs)
    for key in m:
        q[m[key]] = key
    while (len(q)!=0):
        v = []
        cnt = min(k, size)
        for ind in range(cnt):
            if len(q)==0:
                return ""
            t = q.pop(0)
            res.append(t)
            if (t > 0):
                t = t -1
                v.append(t)
            --len
        
        # for (auto a : v) q.push(a)
    
    return res

s = "aaadbbcc"
k = 2
rearrangeString(s,k)