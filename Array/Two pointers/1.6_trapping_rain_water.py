# Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.

# Logic- at any position x of bar, water stored will be min(Lmax, Rmax) - height[x] or 0 if -ve
# Approach 1 can be to compute Lmax and Rmax for each position in two seperate array
#in this way time complexity would be O(n) space o(n)

# Approach 2
# using 2 pointers, u dont need to know both Lmax, Rmax at given pos , u just need min of both.
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) -1
        lmax, rmax = height[l], height[r]
        res = 0
        while l < r:
            if lmax < rmax:
                l += 1
                res += lmax - height[l] if lmax - height[l] > 0 else 0
                lmax = max(lmax, height[l])
                # we could also write , which would meant same 
                # lmax = max(lmax, height[l])
                # res += lmax- height[l]

            else:
                r -= 1
                res += rmax - height[r] if rmax - height[r] > 0 else 0
                rmax = max(rmax, height[r])
        return res
        