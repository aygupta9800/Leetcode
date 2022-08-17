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
    
    def partition(self, lst, left, right, pivot_index):
        pivot = lst[pivot_index][1]
        #Swap pivot node with right most node:
        lst[right], lst[pivot_index] = lst[pivot_index], lst[right]
        
        p = left
        i = left
        
        while i < right:
            curr = lst[i]
            dist = curr[1]
            if dist < pivot:
                #Swap the ith point with p
                lst[p], lst[i] = lst[i],lst[p]
                p += 1
            i += 1
    
        # DONT FORGET TO PUT PIVOT BACK
        # Swap p with pivot right elem
        lst[p], lst[right] = lst[right], lst[p]
        
        return p

    
    def quickselect(self, lst, left, right, k):
        pivot_index = random.randint(left, right)
        p = self.partition(lst, left, right, pivot_index)
        if p == k:
            return [i[0] for i in lst[:p]]
        elif p >k:
            return self.quickselect(lst, left, p-1, k)
        else:
            return self.quickselect(lst,p+1,right, k)

         
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points
        lst = [(i, self.dist(i)) for i in points]
        return self.quickselect(lst,0, len(points) -1, k)
    



# Appraoch 1: Using max heap nlogk
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:  
        return heapq.nsmallest(k, points, key= lambda x: x[0]*x[0] + x[1]*x[1])