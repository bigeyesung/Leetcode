#iterate the loop
#if num-> num*level
#if not: go inside and level+=1
class Solution():
    def __init__(self):
        self.ans = []
    def mytest(self,arr,level):
        for item in arr:
            if not isinstance(item,list):
                # add item
                self.ans.append(item*level)
            else:
                # go to next level
                self.mytest(item,level+1)
    def mywrapper(self, arr):
        level = 1
        self.mytest(arr, level)

    def get(self):
        return sum(self.ans)

if __name__ == "__main__":
    sol = Solution()
    arr = [[1,1],2,[1,1]]
    sol.mywrapper(arr)
    ret = sol.get()
    print(ret)
