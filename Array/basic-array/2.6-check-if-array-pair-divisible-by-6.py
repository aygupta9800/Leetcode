# Approach 1(My own soln)
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        if len(arr) % 2 == 1: return False
        n = len(arr)
        # for x in range(n):
        #     arr[x] = arr[x] % k
        
        dic = defaultdict(int)
        
        count = 0
        for i in arr:
            # print(dic)
            key = k - (i % k)
            # For key = k, we will map it to 0 in hashmap
            # so not to have ambuigity for num =0 or k case
            if key == k:
                key = 0
            if key in dic and dic[key] > 0:
                count += 1
                dic[key] -= 1
            else:
                dic[i%k] += 1
        return count == n//2 
                
                
                