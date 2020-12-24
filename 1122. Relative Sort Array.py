import collections
class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr = []
        counter1 = collections.Counter(arr1)
        #Time: O(N2+N1+C1)
        #S:O(N1)
        #based on arr2 to assign num
        for num in arr2:
            counts = counter1[num]
            arr.extend([num]*counts)
            del counter1[num]
        #iterate counter1:
        for key in counter1:
            counts = counter1[key]
            arr.extend([key]*counts)
        return arr
if __name__ == "__main__":
    tmp = "atach"
    tmp=tmp.replace("a","",1)
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6]
    sol = Solution()
    ret = sol.relativeSortArray(arr1,arr2)
    print(ret)
