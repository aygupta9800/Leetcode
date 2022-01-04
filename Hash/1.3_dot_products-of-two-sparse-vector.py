# Given two sparse vectors, compute their dot product.

# Implement class SparseVector:

# SparseVector(nums) Initializes the object with the vector nums
# dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
# A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

# Follow up: What if only one of the vectors is sparse?
class SparseVector:
    """
    [(0,1), (2,2), (3,3)] [(1,3), (3,4)]
    """
    def __init__(self, nums: List[int]):
        self.dic = {i:a for i,a in enumerate(nums) if a != 0 }
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dic2 = vec.dic
        ans = 0
        # print(self.dic)
        # print(vec.dic)
        if len(self.dic) <= len(dic2):
            for index, value in self.dic.items():
                if index in dic2:
                    ans += value * dic2[index]
        else:
            for index, value in dic2.items():
                if index in self.dic:
                    ans += value *self.dic[index]
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)