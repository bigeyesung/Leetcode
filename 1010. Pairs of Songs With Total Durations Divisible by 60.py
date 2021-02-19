import collections
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter, cnt = collections.Counter(i % 60 for i in time), 0
        #get the mod pairs
        for t in counter:
            if 0 < t < 30: cnt += counter[t] * counter[60-t]
        # mod==30, and mod==0, are special cases, we find pairs in their own group. C(n,2)
        return cnt + counter[30]*(counter[30]-1)//2 + counter[0]*(counter[0]-1)//2

if __name__ == "__main__":
    sol=Solution()
    arr=[60,30,150,100,40,80,120]
    sol.numPairsDivisibleBy60(arr)