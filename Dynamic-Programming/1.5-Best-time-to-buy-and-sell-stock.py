# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Approach1 : keeping track of min price and max profit in linear search.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        """
        min_buy = sys.maxsize
        max_profit = 0
        
        for i, price in enumerate(prices):
            if price > min_buy:
                max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)
        return max_profit