def SetArrs(nums):
    used = [False]*len(nums)

    def MakeWord(length, subArr):
        if len(subArr)==length:
            totalArrs.append(subArr.copy())
            return
        
        for ind in range(len(nums)):
            if used[ind]:
                continue
            used[ind]=True
            subArr.append(nums[ind])
            MakeWord(length,subArr)
            subArr.pop()
            used[ind]=False

    for length in range(1,len(nums)+1):
        MakeWord(length,[])

nums=["a","b"]
totalArrs=[]
SetArrs(nums)
print(totalArrs)
