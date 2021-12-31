# Using Hashmap O(n+m) time and space complexity
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def intersectHelper(nums1, nums2):
            result = []
            countMap = Counter(nums1)
            for i in range(0, len(nums2)):
                if nums2[i] in countMap and countMap[nums2[i]] >0:
                    result.append(nums2[i])
                    countMap[nums2[i]] -= 1
            return result
            
        if len(nums1) < len(nums2):
            return intersectHelper(nums1, nums2)
        else:
            return intersectHelper(nums2, nums1)

# Followup Questions if both the input array are sorted or if we need output in sorted order
# Appraoch 2 sorting
# Java soln
# public int[] intersect(int[] nums1, int[] nums2) {
#     Arrays.sort(nums1);
#     Arrays.sort(nums2);
#     int i = 0, j = 0, k = 0;
#     while (i < nums1.length && j < nums2.length) {
#         if (nums1[i] < nums2[j]) {
#             ++i;
#         } else if (nums1[i] > nums2[j]) {
#             ++j;
#         } else {
#             nums1[k++] = nums1[i++];
#             ++j;
#         }
#     }
#     return Arrays.copyOfRange(nums1, 0, k);