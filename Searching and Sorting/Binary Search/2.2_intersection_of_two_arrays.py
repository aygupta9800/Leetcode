#Using 2 sets O(n+m) time complexity space complexity
class Solution:
    def intersectionHelper(self, set1, set2):
        return [x for x in set1 if x in set2]
        
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        if len(set1) < len(set2):
            return self.intersectionHelper(set1, set2)
        else:
            return self.intersectionHelper(set2, set1)

# This is a Facebook interview question.
# They ask for the intersection, which has a trivial solution using a hash or a set.

# Then they ask you to solve it under these constraints:
# O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
# You are told the lists are sorted.

# function intersections(l1, l2) {
#     l1.sort((a, b) => a - b) // assume sorted
#     l2.sort((a, b) => a - b) // assume sorted
#     const intersections = []
#     let l = 0, r = 0;
#     while ((l2[l] && l1[r]) !== undefined) {
#        const left = l1[r], right = l2[l];
#         if (right === left) {
#             intersections.push(right)
#             while (left === l1[r]) r++;
#             while (right === l2[l]) l++;
#             continue;
#         }
#         if (right > left) while (left === l1[r]) r++;
#          else while (right === l2[l]) l++;
        
#     }
#     return intersections;
# }