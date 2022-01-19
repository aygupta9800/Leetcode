# Approach1 using stack
# O(n) time O(n) space 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        
        for i in range(n-1, -1, -1):
            temp = temperatures[i]
            while len(stack) != 0 and stack[-1][0] <= temp:
                stack.pop()
            if len(stack) == 0:
                temperatures[i] = 0
            else:
                hot_temp = stack[-1]
                temperatures[i] = hot_temp[1]-i
            stack.append((temp, i))
        return temperatures