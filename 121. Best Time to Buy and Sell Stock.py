class Solution:
    def maxProfit(self, prices):
        
        # It is impossible to have stock to sell on first day, so -infinity is set as initial value
        init_hold, init_not_hold = -float('inf'), 0
        
        prev_hold, prev_not_hold = init_hold, init_not_hold
        
        for stock_price in prices:
            
            # either keep in hold, or just buy today with stock price
            cur_hold = max(prev_hold, -stock_price)
            
            # either keep in not holding, or just sell today with stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)
            
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
        
		# maximum profit must be in not-hold state
        return cur_not_hold if prices else 0

#The heuristic is that as long as current price is higher than previous lowest price, 
# max profit could be updated. So I use "buy" to track previous lowest 
# price (indicating we can buy in that time) and "ans" to track max profit we have achieved so far.

    def maxProfit2(self, prices):
        buy, ans = float('inf'), 0
        for p in prices:
            buy, ans = min(buy, p), max(ans, p-buy)
        return ans

    def test(self, prices):
        buy, ans = float('inf'), 0
        for cur_p in prices:
            buy, ans = min(cur_p, buy), max(ans, cur_p-buy)

if __name__ == "__main__":
    sol = Solution()
    arr = [7,1,6]
    ret = sol.maxProfit2(arr)
    print(ret)