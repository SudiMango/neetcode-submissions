class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        max_profit = 0
        curr_max = 0

        l = 0
        r = 0

        while True:
            if r == len(prices):
                return max_profit
            
            if l == r:
                if r + 1 == len(prices):
                    return max_profit
                else:
                    r += 1
            
            if prices[r] - prices[l] < 0:
                l += 1
            else:
                curr_max = prices[r] - prices[l]
                if curr_max > max_profit:
                    max_profit = curr_max
                r += 1


        return max_profit