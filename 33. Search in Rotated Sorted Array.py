#the pivot separates the array to 2 subarrays.
#Each subarray is increasing order
#idea is we decide which sub array we want to go, then do binary search in that sub array


#nums = [4,5,6,7,0,1,2], target = 0
#input: array length>=0, integers
#output: bool

#corner cases: empty array, one-element array

#while-loop: left, right pointers to get middle
    #if middle == target: reture true
    #elif middle>=leftptr:(if left side is in increasing order)
        #if target is in the left section range(leftptr, middle):
        #   set rightptr = middle-1
        #else:
        #   set leftptr = middle+1
    #else: (if right side is in increasing order)
        #if target is in the right section range(middle,rightptr):
        #   set leftptr = middle+1
        #else:
        #   set rightptr = middle-1
   

#return -1

class Solution:
    def search(self, nums:, target):
        left, right = 0, len(nums)-1
        while(left<=right):
            mid = (left+right)//2
            #found it
            if nums[mid]==target:
                return mid
            #if right-side is increasing order
            elif nums[mid]<=nums[right]:
                #normal increasing seciton
                if nums[mid]<=target and target<=nums[right]:
                    left=mid+1
                #pivot section
                else:
                    right=mid-1
            #if left-side is increasing order
            else:
                #normal increasing seciton
                if nums[left]<=target and target<=nums[mid]:
                    right=mid-1
                #pivot section
                else:
                    left=mid+1
        return -1