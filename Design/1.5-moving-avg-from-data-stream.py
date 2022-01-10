# 346. Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Implement the MovingAverage class:

# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.
 

# Example 1:

# Input
# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]
# Output
# [null, 1.0, 5.5, 4.66667, 6.0]

# Explanation
# MovingAverage movingAverage = new MovingAverage(3);
# movingAverage.next(1); // return 1.0 = 1 / 1
# movingAverage.next(10); // return 5.5 = (1 + 10) / 2
# movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
# movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

# Approach 1
# Using deque 
# TIme O(1), space O(N) where N is size of the moving window
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        # number of elements seen so far
        self.window_sum = 0
        self.count = 0
        

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        
        self.window_sum = self.window_sum - tail + val
        
        return self.window_sum / min(self.size, self.count)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# Approach 2 Using circular queue
"""
 The key to the implementation is the correlation between the index of head and tail elements, which we could summarize in the following formula:
tail = (head + 1) % size
"""
"""
The major advantage of circular queue is that by adding a new element to a full circular queue, it automatically discards the oldest element. Unlike deque, we do not need to explicitly remove the oldest element.
Another advantage of circular queue is that a single index suffices to keep track of both ends of the queue, unlike deque where we have to keep a pointer for each end.
"""
# Time Complexity: O(1), as we can see that there is no loop in the next(val) function.

# Space Complexity: O(N), where NN is the size of the circular queue.
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = [0] * self.size
        self.head = 0
        self.window_sum = 0
        # number of elements seen so far
        self.count = 0
        

    def next(self, val: int) -> float:
        self.count += 1
        # calculate the new sum by shifting the window
        # self.queue.append(val)
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next node
        self.head = (self.head + 1) % size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)
