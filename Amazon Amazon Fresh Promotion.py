#Input: codeList = [[apple, apple], [banana, anything, banana]] shoppingCart = [orange, apple, apple, banana, orange, banana]
#Input: codeList = [[apple, apple], [apple, apple, banana]] shoppingCart = [apple, apple, apple, banana]

codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["orange", "apple", "apple", "banana", "orange", "banana"]
newCodeList=[]
ret=[] #start,end index
def findWinner(codeList,shoppingCart):
    for ind in range(len(codeList)):
        tmp=[]
        for fruit in codeList[ind]:
            if fruit!="anything":
                tmp.append(fruit)
        #if we have "anything"-> separate the list
        if len(tmp)!=len(codeList[ind]):
            for tmpcode in tmp:
                newCodeList.append("".join(tmpcode))
        else:
            newCodeList.append("".join(codeList[ind]))

    shoppingCart="".join(shoppingCart)
    #appleappleapplebanana
    startIdx=0
    for code in newCodeList:
        #do sliding window
        #appleapple
        windowSize=len(code)
        for ind in range(startIdx,len(shoppingCart)-(windowSize-1)):
            window=shoppingCart[ind:ind+windowSize]
            if window == code:
                ret.append([ind,ind+windowSize-1])
                startIdx=ind+windowSize
                break
    # return ret
    return len(ret)==len(newCodeList)    
        

ret=findWinner(codeList, shoppingCart)
print(ret)