#Approach 3: Single queue O(n)
# Time complexity : O(n)O(n). The algorithm removes n elements and
# inserts n + 1n+1 elements to q1 , where n is the stack size.
# This gives 2n + 12n+1 operations. The operations add and
#  remove in linked lists has O(1)O(1) complexity.
"""
When we push an element into a queue, it will be stored at back of the queue
due to queue's properties. But we need to implement a stack,
where last inserted element should be in the front of the queue,
not at the back. To achieve this we can invert the order of queue elements when pushing a new element.
"""

class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
         return self.queue[0]

    def empty(self) -> bool:
        return not len(self.queue)


#Approach 2: Using 2 queues with push O(n) pop O(1) push
"""
public void push(int x) {
    q2.add(x);
    top = x;
    while (!q1.isEmpty()) {                
        q2.add(q1.remove());
    }
    Queue<Integer> temp = q1;
    q1 = q2;
    q2 = temp;
}
"""
#Approach 1: Using 2 queues with pop O(n) push O(1)
"""
private Queue<Integer> q1 = new LinkedList<>();
private Queue<Integer> q2 = new LinkedList<>();
private int top;

// Push element x onto stack.
public void push(int x) {
    q1.add(x);
    top = x;
}
"""

# Approach 1 Using queue as linklist time O(1) (NOT SURE)
# class Stack(object):
#     def __init__(self):
#         self.queue = None

#     def push(self, x):
#         q = collections.deque()
#         q.append(x)
#         q.append(self.queue)
#         self.queue = q

#     def pop(self):
#         self.queue.popleft()
#         self.queue = self.queue.popleft()

#     def top(self):
#         return self.queue[0]

#     def empty(self):
#         return not self.queue