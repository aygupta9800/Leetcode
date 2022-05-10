class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # two heaps, one for avail, one for unavaila
        res = [0] * len(tasks)
        
        available = [(servers[i], i) for i in range(len(servers))]
        heapq.heapify(available)
        unavailable = []
        t  = 0
        for i in range(len(tasks)):
            # as time can be more than i 
            t = max(t, i)
            
            if len(available) == 0:
                # advance time to min time when server becomes available
                t = unavailable[0][0]
            # put all available servers from unavail heap
            while unavailable and unavailable[0][0] <= t:
                time_free, weight, index = heapq.heappop(unavailable)
                heapq.heappush(available, (weight, index))
                
            weight, index = heapq.heappop(available)
            heapq.heappush(unavailable, (tasks[i] + t, weight, index))
            res[i] = index
            # t += 1
        return res