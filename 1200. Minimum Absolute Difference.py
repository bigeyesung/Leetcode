import collections

class Solution:
    def minimumAbsDifference(self, arr):
        #Time: O(n*log(n)+n*m)
        #Space: O(n)
        #sort():O(n*log(n))
        #m: value length of table[key]

        #return list should be in ascending order
        
        #corner case: empty arr
        #corner case: only one ele
        table = collections.defaultdict(list)
        minDiff = float("inf")
        #sort the array
        arr.sort()
        #iterate every 2 adjacent eles
        for ind in range(0,len(arr)-1):
            curDiff = arr[ind+1]-arr[ind]
            #save the length to a length table
            table[curDiff].append([arr[ind],arr[ind+1]])
        
            minDiff=min(minDiff, curDiff)
        
        #get the min length arr from table
        return table[minDiff]


    def minimumAbsDifference1(self, arr):
        #Time: O(n*log(n)+n)
        #Space: O(n)
        #sort():O(n*log(n))
        #append(): O(1)

        #sort arr
        arr.sort()
        ret = []
        maxDiff=arr[-1]-arr[0]
        for ind in range(0,len(arr)-1):
            curDiff=arr[ind+1]-arr[ind]
            if maxDiff==curDiff:
                ret.append([arr[ind],arr[ind+1]])
            elif maxDiff>curDiff:
                maxDiff=curDiff
                ret = [[arr[ind],arr[ind+1]]]
        return ret