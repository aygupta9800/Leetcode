#Approach 2: Using stack: O(n)
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if i< len(s) -1 and s[i] == s[i+1]:
                i += 2
            elif len(stack) > 0 and stack[-1] == s[i]:
                stack.pop()
                i += 1
            else:
                stack.append(s[i])
                i += 1
        res = ""
        while stack:
            res = stack.pop() + res
        return res

#Approach 1 O(n2) 
class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while i < len(s) -1:
            if s[i] == s[i+1]:
                s = s[:i]+s[i+2:]
                if i > 0:
                    i -= 1
            else:
                i += 1
        return s