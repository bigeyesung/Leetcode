def palindromePairs(words):    
    wordict = {}
    res = [] 
    for i in range(len(words)):
        wordict[words[i]] = i
    for i in range(len(words)):
        for j in range(len(words[i])+1):
            tmp1 = words[i][:j]
            tmp2 = words[i][j:]
            print(tmp1)
            print(tmp2)
            if tmp1[::-1] in wordict and wordict[tmp1[::-1]]!=i and tmp2 == tmp2[::-1]:
                res.append([i,wordict[tmp1[::-1]]])
            if j!=0 and tmp2[::-1] in wordict and wordict[tmp2[::-1]]!=i and tmp1 == tmp1[::-1]:
                res.append([wordict[tmp2[::-1]],i])
                
    return res
tmp = "abcd"
tmp2 = tmp[::-1]
arr = ["abcd","dcba"]
res = palindromePairs(arr)
print(res)