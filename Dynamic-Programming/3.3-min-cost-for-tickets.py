# Approach 1 top down with cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """ 
        for every index we have 3 options to choose
        and then we move to index corresding to when the plan finishes to calculate remaining cost
        dp(i)=min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])
        
        """
        dp = {}
        
        N = len(days)
        durations = [1, 7, 30]
        
        def minCost(i):
            if i in dp:
                return dp[i]

            if i >= N:
                return 0

            dp[i] = float('inf')
            # we can start j above since our duration is increasing order
            # so next day for next duration will be greater or equal to last
            # duration next day
            j = i
            for d, c in zip(durations, costs):
                # next index j
                # j = i
                while j < N and days[j] < days[i] + d:
                    j += 1
                if j >= N:
                    dp[i] = min(dp[i], c)
                else:
                    dp[i] = min(dp[i], c+ minCost(j))
            return dp[i]
        return minCost(0)

# Approach 2 with bottom up approach
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """ 
        for every index we have 3 options to choose
        and then we move to index corresding to when the plan finishes to calculate remaining cost
        dp(i)=min(dp(i+1)+costs[0],dp(i+7)+costs[1],dp(i+30)+costs[2])
        
        """
        dp = {}
        
        N = len(days)
        durations = [1, 7, 30]
        
        # # we go reverse as we can use later values to find earlier values cost
        for i in range(N -1, -1, -1):
            # We have 3 options
            dp[i] = float('inf')
            # we can start j above since our duration is increasing order
            # so next day for next duration will be greater or equal to last
            # duration next day
            j = i
            for d,c in zip(durations, [costs[0], costs[1], costs[2]]):
                # what the next j
                # j = i
                while j< len(days) and days[j] < days[i]+ d:
                    j+=1
                # in case j is out of bound or j was not initially found
                dp[i] = min(dp[i], c+ dp.get(j, 0))
        return dp[0]