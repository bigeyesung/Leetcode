def fiveStartReviews(productRatings, ratingsThreshold):
    curr=0
    for rate in productRatings:
        num= rate[0]/rate[1]
        curr+=num
        
    result=0
    totalProducts=len(productRatings)
    reqSum=ratingsThreshold*totalProducts *1.0/100
    #if already achieve target
    if curr>=reqSum:
        return 0

    cSum=0
    while(cSum<reqSum):
        cSum=0
        maxCon=0
        productItem=-1
        #iterate the totalProducts, find out which one has the most largest diff(c),
        #find that index and assign it to productItem
        for ind in range(totalProducts):
            c = (productRatings[ind][0]+1)/(productRatings[ind][1]+1)-(productRatings[ind][0])/(productRatings[ind][1])
            if maxCon<c:
                maxCon=c
                productItem=ind
            cSum+=(productRatings[ind][0])/(productRatings[ind][1])
        #change productItem value, and update cSum
        cSum=cSum-(productRatings[productItem][0])/(productRatings[productItem][1])
        productRatings[productItem][0]+=1
        productRatings[productItem][1]+=1
        cSum=cSum+(productRatings[productItem][0])/(productRatings[productItem][1])
        result+=1
    return result
    
     
    #change the Threshold to Threshold*len(productRatings)
    #if the product Rating == 1-> subtract from Threshold
productRatings = [[4,4], [3, 6],[1,2] ]
ratingsThreshold = 77
# count=fiveStartReviews(productRatings,ratingsThreshold)
# productRatings = [[2,4], [1, 2] ]
# ratingsThreshold = 51
count=fiveStartReviews(productRatings,ratingsThreshold)