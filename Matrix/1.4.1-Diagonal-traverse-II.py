class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        res = []
        # since we dont know range of r+c we start with min
        for r in range(m):
            n = len(nums[r])
            for c in range(n):
                if len(res) <= r +c:
                    res.append([])
                res[r+c].append(nums[r][c])   
        l = []
        for r in res:
            l.extend(reversed(r))
        return l