class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        rotatedMap = {
            "0": "0", "1": "1", "8": "8", "6": "9", "9": "6"
        }
        
        def backtrack(path="", low=0, high=n-1):
            #Base condn
            if low > high:
                if len(path) == 1 or path[0] != "0":
                    # print(":",path)
                    res.append(path)
                return
            for key, value in rotatedMap.items():
                if low == high:
                    if key in ["0", "1", "8"]:
                        backtrack(path[:low]+key+path[low:], low +1, high)
                else:
                    backtrack(key+ path + value, low+1, high -1)
                
        
        res = []
        if n< 1:
            return res
        
        backtrack()
        return res
