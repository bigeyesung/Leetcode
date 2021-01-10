class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
    #one guy from left(left ptr)
    #one guy from right(right ptr)
    #meet in the middle
        left, right, n = 0, len(arr)-1, len(arr)
        while(left+1<n and arr[left]<arr[left+1]):
            left+=1
        while(right-1>=0 and arr[right]<arr[right-1]):
            right-=1
        return 0<left==right<n-1
#         if len(arr)<3:
#             return False

#         for ind in range(1,len(arr)-1):
#             #left side
#             leftCheck = True
#             #right side
#             for ind1 in range(0,ind):
#                 if arr[ind1]>=arr[ind1+1]:
#                     leftCheck = False
#                     break
#             rightCheck = True
#             #ind = 6, len(arr)=8
#             for ind2 in range(ind, len(arr)-1):
#                 if arr[ind2]<=arr[ind2+1]:
#                     rightCheck = False
#                     break
#             if rightCheck and leftCheck:
#                 return True

#         return False


def CheckValidMountain(arr):
    leftPtr, rightPtr = 0, len(arr)-1
    #go from left side
    while(arr[leftPtr]<arr[leftPtr+1] and leftPtr < len(arr)-1):
        leftPtr+=1
    #go from right side
    while(arr[rightPtr]<arr[rightPtr-1]] and rightPtr>=1):
        rightPtr-=1
    #check if leftPtr and rightPtr in the same index
    if 0<leftPtr==rightPtr<len(arr)-1:
        return True
    else:
        return False