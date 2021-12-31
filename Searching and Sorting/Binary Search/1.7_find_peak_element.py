#o(1) space, o(logn) binary
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        . We start off by finding the middle element, mid from the given numsnums array.
         If this element happens to be lying in a descending sequence of numbers. 
         or a local falling slope(found by comparing nums[i]nums[i] to its right neighbour),
        it means that the peak will always lie towards the left of this element.
         Thus, we reduce the search space to the left of midmid(including itself) and perform the same process on left subarray.
        TIme compelxity O(n), space O(1)
        """
        l, r = 0, len(nums) -1
        while l < r :
            mid = (l +r) // 2  
            if nums[mid] > nums[mid +1]:
                r= mid
            else:
                l = mid +1
        return l

#Recursive binary search JAva
# public class Solution {
#     public int findPeakElement(int[] nums) {
#         return search(nums, 0, nums.length - 1);
#     }
#     public int search(int[] nums, int l, int r) {
#         if (l == r)
#             return l;
#         int mid = (l + r) / 2;
#         if (nums[mid] > nums[mid + 1])
#             return search(nums, l, mid);
#         return search(nums, mid + 1, r);
#     }
# }

# Another approach by comparing slope both side and return true if its peak
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        . We start off by finding the middle element, midmid from the given numsnums array. If this element happens to be lying in a descending sequence of numbers. or a local falling slope(found by comparing nums[i]nums[i] to its right neighbour), it means that the peak will always lie towards the left of this element. Thus, we reduce the search space to the left of midmid(including itself) and perform the same process on left subarray.
        TIme compelxity O(n), space O(1)
        """
        l, r= 0, len(nums) -1
        while l <= r:
            mid = (l + r) // 2
            prev = float("-inf") if mid == 0 else nums[mid -1]
            nxt =  float("-inf") if mid == len(nums) -1 else nums[mid +1]
            # print( "prev", prev, "mid", mid, "next", nxt)
            
            if prev < nums[mid] and nxt < nums[mid]:
                return mid
            if nxt < nums[mid]:
                r = mid -1
            else:
                l = mid +1