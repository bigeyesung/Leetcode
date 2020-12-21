arr = [[0, 30],[5, 10],[15, 20]]

def test(arr):
    num = 1
    #sort the list first
    for ind in range(len(arr)-1):
        if arr[ind+1][1]<=arr[ind][1]:
            num+=1
    return num

ret = test(arr)
print(ret)