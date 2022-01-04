# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane 
# and an integer k, return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
#Approach 2: Using Quick select algo
# Time: avg O(n), worst : O(n^2)
# space: O()
class Solution:
    """
    Since order of k element can be anything we can use
    quickselect algo
    """
    
    def dist(self, pt):
        return pt[0] ** 2 + pt[1] ** 2
    
    def find(self, lst, k):
        if len(lst) == k:
            return [i[0] for i in lst]
        rand_tup = random.choice(lst)
        pivot = rand_tup[1]
        
        i = 0
        left = []
        right = []
        equal = []
        
        while i < len(lst):
            curr = lst[i]
            dist = curr[1]
            if dist < pivot:
                left.append(curr)
            elif dist > pivot:
                right.append(curr)
            else:
                equal.append(curr)
            i += 1
        len_left = len(left)
        if len_left == k:
            return [i[0] for i in left]
        elif len_left + len(equal) == k:
            return [i[0] for i in left] + [i[0] for i in equal]
        elif len_left >k:
            return self.find(left, k)
        else:
            return [i[0] for i in left] + [i[0] for i in equal] + self.find(right, k-len_left-len(equal))
             
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lst = [(i, self.dist(i)) for i in points]
        return self.find(lst, k)


# Appraoch 1: Using max heap nlogk
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:  
        return heapq.nsmallest(k, points, key= lambda x: x[0]*x[0] + x[1]*x[1])