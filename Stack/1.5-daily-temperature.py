#Approach2 Using stack from front
# we keep pop until stack top is warmer than curr day
# then we push curr day
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
            # Pop until the current day's temperature is not
            # warmer than the temperature at the top of the stack
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer

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