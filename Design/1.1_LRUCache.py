# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.

# Example 1:
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Time complexity : \mathcal{O}(1)O(1) both for put and get.

# Space complexity : \mathcal{O}(capacity)O(capacity) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache= {}
        self.head, self.tail = DLinkedNode(), DLinkedNode
        self.head.next, self.tail.prev = self.tail, self.head
    
    def remove_node(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
    
    def add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def move_to_head(self, node):
        self.remove_node(node)
        self.add_node(node)
        
    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node:
            return -1
        self.move_to_head(node)
        return node.value
    
    def pop_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node
        
    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if not node:
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value
            
            self.cache[key] = newNode
            self.add_node(newNode)
            self.size += 1
            if self.size > self.capacity:
                #pop the tail
                tail = self.pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            #update the value
            node.value = value
            self.move_to_head(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4