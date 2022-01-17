

#Approach 1 using peak valley concept
# Complexity Analysis
# Time complexity : O(n)O(n). Single pass.
# Space complexity : O(1)O(1). Constant space required.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Peak valley approach
        Mathmatically TotalProfit max = sum(height(peak(i))-height(valley(i)))
        """
        valley = prices[0]
        peak= prices[0]
        maxProfit = 0
        i = 0
        n= len(prices)
        # we break at i = n-2 as after that we cant do buy and sell. it will go in infinite loop as no terminating condn
        while i < n-1:
            #Reach till valley
            while i< n-1 and prices[i] >= prices[i+1]:
                i+= 1
            valley = prices[i]
            #reach till next peak
            while i < n-1 and prices[i] <= prices[i+1]:
                i+= 1
            peak = prices[i]
            maxProfit += peak - valley
        return maxProfit

# Approach 2 single one-pass
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 0
        n= len(prices)
        while i < n-1:
            #if next number is larger than only profit is possible
            if prices[i] < prices[i+1]:
                maxProfit += prices[i+1] - prices[i]
            i += 1
        return maxProfit
        