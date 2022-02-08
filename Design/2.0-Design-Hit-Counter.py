# https://leetcode.com/problems/design-hit-counter/

# Design a hit counter which counts the number of hits received in the past 5 minutes (i.e., the past 300 seconds).

# Your system should accept a timestamp parameter (in seconds granularity), and you may assume that calls are being made to the system in chronological order (i.e., timestamp is monotonically increasing). Several hits may arrive roughly at the same time.

# Approach 2 using (timestamp, count) in deque
class HitCounter:

    def __init__(self):
        self.q = collections.deque([])
        self.totalHits = 0

    def hit(self, timestamp: int) -> None:
        if not self.q or self.q[-1][0] != timestamp:
            self.q.append([timestamp, 1])
        else:
            self.q[-1][1] += 1
        self.totalHits += 1

    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp- self.q[0][0] >= 300:
            time, hits = self.q.popleft()
            self.totalHits -= hits
        return self.totalHits

if __name__== "__main__":
    hitCounter = HitCounter()
    hitCounter.hit(1);       # hit at timestamp 1.
    hitCounter.hit(2);       # hit at timestamp 2.
    hitCounter.hit(3);       # hit at timestamp 3.
    print(hitCounter.getHits(4));   # get hits at timestamp 4, return 3.
    hitCounter.hit(300);     # hit at timestamp 300.
    print(hitCounter.getHits(300)); # get hits at timestamp 300, return 4.
    print(hitCounter.getHits(301)); # get hits at timestamp 301, return 3.




# Approach 1 Using queue
import collections
class HitCounter:

    def __init__(self):
        self.q = collections.deque([])

    def hit(self, timestamp: int) -> None:
        # while self.q and timestamp- self.q[0] >= 300:
        #     self.q.popleft()
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.q and timestamp- self.q[0] >= 300:
            self.q.popleft()
        return len(self.q)    
