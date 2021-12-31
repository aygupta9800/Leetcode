# Approach 2: Two pointers
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        # In python, we use list as a string builder.
        rotatedStringBuilder = []
        rotatedMap = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        left, right = 0, len(num) -1
        #Remember that we want to loop backward in string
        while left <= right:
            if num[left] not in rotatedMap or rotatedMap[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        
        return True

# Approach 1 reverse with corresponding digit (Make a rotated Copy)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        # In python, we use list as a string builder.
        rotatedStringBuilder = []
        
        #Remember that we want to loop backward in string
        for c in reversed(num):
            if c in {'0', '1', '8'}:
                rotatedStringBuilder.append(c)
            elif c == '6':
                rotatedStringBuilder.append('9')
            elif c == '9':
                rotatedStringBuilder.append('6')
            else: # invalid digit
                return False
        
        rotatedString = "".join(rotatedStringBuilder)
        return rotatedString == num