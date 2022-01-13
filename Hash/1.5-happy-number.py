
# Approach 2: Floyd's Cycle-Finding Algorithm
# Time complexity : O(\log n)O(logn). Builds on the analysis for the previous approach, except this time we need to analyse how much extra work is done by keeping track of two places instead of one, and how many times they'll need to go around the cycle before meeting.
# we're treating the length of the chain to the cycle as insignificant compared to the cost of calculating the next value for the first n. Therefore, the only thing we need to do is show that the number of times the runners go back over previously seen numbers in the chain is constant.
# Space O(1)

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total = 0
            while n > 0:
                # digit, n = n %10, n // 10
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total
        
        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1
        


# Approach 1
# Time complexity : O(243 * 3 + log n + loglog n + logloglog n)+...... = O(logn)
# Space complexity : O(logn). Closely related to the time complexity, and is a measure of what numbers we're putting in the HashSet, and how big they are. For a large enough nn, the most space will be taken by nn itself.
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total = 0
            while n > 0:
                # digit, n = n %10, n // 10
                n, digit = divmod(n, 10)
                total += digit ** 2
            return total
        
        seen = set()
        while n != 1 or n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1
        