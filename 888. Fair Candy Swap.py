'''
这道题说爱丽丝和鲍勃两人有不同大小的糖果，现在要让两人交换一个糖果，使得交换后两人的糖果总量相同，
而且限定了两人初始时的糖果总量不相同，并且一定会有解。若我们仔细观察题目中给的例子，
可以发现所有例子中起始时 Alice 和 Bob 两人的糖果总量的差值一定时偶数，
这是 make sense 的，因为最终两人的糖果总量时要相同的，
那么起始时的量差就应该能平均分为两部分，一部分来弥补轻的一方，一部分来抵消重的一方。
那么有了这个 diff，我们只需要在两个数组中查找差值为 diff 的两个数字了，其实就是 [Two Sum]的变种，
使用一个 HashSet 先来保存数组 A 中所有的数字，然后遍历数组B中的每个数字 num，查找 HashSet 中否存在 num+diff 即可
'''



class Solution:
    def fairCandySwap(self, A, B):
        #final candies for each ppl is 3
        dif = (sum(A) - sum(B)) // 2
        #set(A),set(B): array with "exchange amount"
        #set(A)=1: A needs to release 1 candy
        #set(B)=2: B needs to release 2 candy
        #exchange amountA-exchange amountB = dif-> exchange amountA=exchange amountB+dif
        A = set(A)
        for b in set(B):
            if dif + b in A:
                return [dif + b, b]


if __name__ == "__main__":
    sol = Solution()
    #A has totally 2 candies
    #B has totally 4 candies
    A = [1,1]
    B = [2,2]
    ret = sol.fairCandySwap(A,B)
    print(ret)