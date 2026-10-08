class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0
        profit = 0
        while r<len(prices):
            if prices[l] > prices[r]:
                # print(l,r)
                l = r
                r+=1
            else:
                profit = prices[r] - prices[l]
                # print(profit,l,r)
                if profit > max_profit:
                    max_profit = profit
                r+=1
        return max_profit
