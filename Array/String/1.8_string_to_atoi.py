# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Input: s = "4193 with words"
# Output: 4193
# Explanation:
# Step 1: "4193 with words" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
#              ^
# The parsed integer is 4193.
# Since 4193 is in the range [-231, 231 - 1], the final result is 4193.

#Time O(N)
# space O(1)
#soln2
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        index = 0
        n = len(s)
        
        INT_MAX = pow(2,31) -1
        INT_MIN = -pow(2, 31)
        
        #Discard all the spaces from beigninning
        while index < n and s[index] == ' ':
            index += 1
        
        #sign = +1,or -1
        if index < n and s[index] == "+":
            sign = 1
            index += 1
        elif index <n and s[index] == "-":
            sign = -1
            index += 1
        
        # Traverse next digits till next is not digit or end of string
        while index < n and s[index].isdigit():
            digit = int(s[index])
            
            #Check overflow and underflow conditions
            if (result > INT_MAX //10 ) or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            # Append digit
            result = 10 * result + digit
            index += 1
        
        return sign * result
            


# Solution1
class Solution:
    def myAtoi(self, s: str) -> int:   
        st = 0
        sign = 1
        s = s.strip()
        if len(s)<1:
            return 0
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1

        if s[0] == '+':
            sign = +1
            index += 1

        while index<len(s) and s[index].isdigit():
            st = st*10 + int(s[index])
            index += 1

        return min(max(st*sign, -2**31), 2**31-1)



# My solution 1
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i< len(s) and s[i] == ' ':
            i += 1
        if i == len(s):
            return 0
        factor = 1
        if s[i] == '-':
            factor = -1
            i +=1
        elif s[i] == '+':
            i +=1
        if i< len(s) and not s[i].isdigit():
            return 0
        num_str = ''
        num = 0
        while i<len(s) and s[i].isdigit():
            num_str+= s[i]
            i +=1
        if num_str == '':
            return num
        num = factor * int(num_str)
        if num < -1* 2**31:
            num = -1* 2**31
        elif num > 2**31 - 1:
            num = 2**31 -1
        return num
            