def missingNum(nums):
    i=0
    n=len(nums)
    while(i<n):
        print("i:",i)
        print("nums[i]:",nums[i])
        j=nums[i]
        #e.g. 2 != array[2]->swap
        if j<n and j!=nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        else:
            i+=1

arr=[3,0,1]
missingNum(arr)
print(arr)