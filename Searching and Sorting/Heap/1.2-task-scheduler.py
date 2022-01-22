# https://leetcode.com/problems/task-scheduler/

# For each unit of time, the CPU could complete either one task or just be idle.
# However, there is a non-negative integer n that represents the cooldown period
# between two same tasks (the same letter in the array), that is that there must be at
# least n units of time between any two same tasks.
# Return the least number of units of times that the CPU will take
# to finish all the given tasks.

# Example 1:

# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: 
# A -> B -> idle -> A -> B -> idle -> A -> B
# There is at least 2 units of time between any two same tasks.

class Solution:
    """
    to reduce idle time we would like to pick max freq char which is available to execute at current time. so we use maxHeap here.
    we use queue so that we can pop task which is first executed as it 
    will be ready first to again execute among others
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time
        
        count = Counter(tasks)
        # we just need count of each char, doesnt depend which char it is
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        q = deque() # pair of (cnt, time at which it will be again aval)
        #till there is task remaining to execute
        while maxHeap or q:
            time += 1
            # if some task can be executed
            if maxHeap:
                cnt = heapq.heappop(maxHeap) +1
                #if some cnt is still there to execute later
                if cnt:
                    q.append([cnt, time+n])
            # if some char becomes ready to execute again, add it to heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time
            
                    
        
        
        