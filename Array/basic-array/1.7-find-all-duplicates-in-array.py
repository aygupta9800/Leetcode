# Do it in O(n) time + in place
# Approach Negative marking
# Java code
# class Solution {
#     public List<Integer> findDuplicates(int[] nums) {
#         List<Integer> ans = new ArrayList<>();

#         for (int num : nums) {
#             if (nums[Math.abs(num) - 1] < 0) { // seen before
#                 ans.add(Math.abs(num));
#             }
#             nums[Math.abs(num) - 1] *= -1;
#         }

#         return ans;
#     }
# }