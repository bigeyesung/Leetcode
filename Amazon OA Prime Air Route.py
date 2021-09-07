A=[2000,4000,6000]
B=[2000]
minLen=len(A)
larger=len(B)
minArr=A
largerArr=B
if len(B)<=len(A):
    minLen=len(B)
    larger=len(A)
    minArr=B
    largerArr=A
i=0
j=0
maxSum=9000
ret=[]
while(j<minLen):
    if i<larger and minArr[j]+largerArr[i]<=maxSum:
        i+=1
    #if we run til the whole minArr, and did not meet maxSum
    elif i>=larger:
        ret.append((minArr[j],largerArr[i-1]))
        j+=1
        i=0
    else:
        #decrease i
        while(0<=i<larger and largerArr[i]+minArr[j]>maxSum):
            i-=1
        #i is in valid index
        if 0<=i<larger:
            ret.append((minArr[j],largerArr[i]))
            j+=1
        #move to next j and reset i=0
        else:
            j+=1
            i=0



print(ret)