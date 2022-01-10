# You are given two run-length encoded arrays encoded1 and encoded2
# representing full arrays nums1 and nums2 respectively.
# Both nums1 and nums2 have the same length.
# Each encoded1[i] = [vali, freqi] describes the ith segment of nums1, and
# each encoded2[j] = [valj, freqj] describes the jth segment of nums2.

# Return the product of encoded1 and encoded2.

# Example 1:

# Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
# Output: [[6,6]]
# Explanation: encoded1 expands to [1,1,1,2,2,2] and encoded2 expands to [6,6,6,3,3,3].
# prodNums = [6,6,6,6,6,6], which is compressed into the run-length encoded array [[6,6]].

# 1868. Medium
#Approach 1 # two pointers
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        product_encoded = []

        e1_index = 0
        e2_index = 0

        while e1_index < len(encoded1) and e2_index < len(encoded2):
            e1_val, e1_freq = encoded1[e1_index]
            e2_val, e2_freq = encoded2[e2_index]

            product_val = e1_val * e2_val
            product_freq = min(e1_freq, e2_freq)

            encoded1[e1_index][1] -= product_freq
            encoded2[e2_index][1] -= product_freq

            if encoded1[e1_index][1] == 0:
                e1_index += 1

            if encoded2[e2_index][1] == 0:
                e2_index += 1

            if not product_encoded or product_encoded[-1][0] != product_val:
                product_encoded.append([product_val, product_freq])
            else:
                product_encoded[-1][1] += product_freq



        return product_encoded
