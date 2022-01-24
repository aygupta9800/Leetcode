class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        ans = base = 0
        
        while base < N:
            end = base
            #if base is left boundary
            if end +1 <N  and A[end]< A[end+1]:
                # set end to the peak of this mountain
                while end +1 < N and A[end] < A[end+1]:
                    end += 1
                # if the end is really a peak
                if end +1 <N and A[end]> A[end+1]:
                    #set end to right boundary of the mountain
                    while end+1< N and A[end] > A[end+1]:
                        end += 1
                    
                    # Record the ans:
                    ans = max(ans, end-base+1)
            
            # If there is no mountain then end will be base
            # But if its mountain, then end will be new base
            base = max(end, base+1)
        return ans
            