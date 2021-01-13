import collections
class Solution:
    def hasGroupsSizeX(self, deck):
        if not deck:
            return False
        dic = collections.Counter(deck)
        div = min(dic.values())
        if div < 2:
            return False
        for i in range(2, div+1):
            if all(val % i == 0 for val in dic.values()):
                return True
        return False

if __name__ == "__main__":
    deck=[1,1,1,2,2,2,3,3]
    sol=Solution()
    ret=sol.hasGroupsSizeX(deck)
    print(ret)