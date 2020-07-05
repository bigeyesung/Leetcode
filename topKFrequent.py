import collections
def myfunc1(ele):
    return ele[0]

def topKFrequent(words, k):  
    count = collections.Counter(words)

    table = {}
    arr = []
    ans = []
    for word in count:
        frq = count[word]
        if table.get(frq)==None:
            table[frq] = [word]
        else:
            table[frq].append(word)
    for ind,key in enumerate(table):
        tmp = [key,table[key]]
        arr.append(tmp)
    #sort by freq first
    arr.sort(reverse = True,key=myfunc1)
    #sort by lettter second
    for lists in arr:
        lists[1].sort()
    count = 0
    loop_break = False
    for lists in arr:
        if not loop_break:
            for word in lists[1]:
                ans.append(word)
                count += 1
                if count >=k:
                    loop_break = True
                    break
    return ans

arr = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3

ret = topKFrequent(arr,k)
print