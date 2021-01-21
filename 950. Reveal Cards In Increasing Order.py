import collections
class Solution:
    def deckRevealedIncreasing(self, deck):
        N = len(deck)
        que = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            ans[index.popleft()] = card
            if que:
                que.append(que.popleft())

        return ans

if __name__ == "__main__":
    sol=Solution()
    arr=[17,11,2,3,5,7]
    ret=sol.deckRevealedIncreasing(arr)