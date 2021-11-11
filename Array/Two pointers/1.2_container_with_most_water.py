
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
# Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

# Notice that you may not slant the container.
# Time complexity O(n)
def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) -1
    area = 0
    while l < r:
        area = max(min(height[l], height[r]) * (r-l), area)
        if height[l] < height[r]:
            l +=1
        else:
            r -= 1
    return area