class Solution:
    def minSwaps(self, s: str) -> int:
        """
        1. count diff <= 1
        2. if count diff = 1: then bigger fre elem will be the first
        3. if diff = 0 then both can start
        
        Now to know the swap positions:
        we need to check how many 1st are at odd
        and 0's at odd
        2 1s
        1 0's
        1111000
        2 1's
        2 0's
        """
        count1 = count0 = 0
        oddone, oddZero = 0 ,0
        for i in range(len(s)):
            if i%2 == 0:
                if s[i] == '1':
                    oddone += 1
                else:
                    oddZero += 1
            if s[i] == '1':
                count1 += 1
            else:
                count0 += 1
        
        if abs(count1 -count0) > 1:
            return -1
       
        if count1 > count0:
            return oddZero
        elif count1 == count0:
            return min(oddone, oddZero)
        else:
            return oddone
            
        
        # return 
            
            
        