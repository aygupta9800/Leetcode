# Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

# Return a list of all possible strings we could create. Return the output in any order.

 

# Example 1:

# Input: s = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# Time Complexity: O(2^{N} * N where N is the length of S. This reflects the cost of writing the answer.



class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def recursion(s, i, path):
            if i == len(s):
                res.append(path)
                return
            if s[i].isdigit():
                recursion(s, i+1, path+s[i])
            else:
                recursion(s, i+1, path+s[i].lower())
                recursion(s, i+1, path+s[i].upper())
            return
        recursion(s, 0, "")
        return res

#Another iterative approach
# Maintain the correct answer as we increase the size of the prefix of S we are considering.

# For example, when S = "abc", maintain ans = [""], 
# and update it to ans = ["a", "A"], ans = ["ab", "Ab", "aB", "AB"],
#  ans = ["abc", "Abc", "aBc", "ABc", "abC", "AbC", "aBC", "ABC"]
# as we consider the letters "a", "b", "c"
class Solution(object):
    def letterCasePermutation(self, S):
        ans = [[]]

        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in xrange(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n+i].append(char.upper())
            else:
                for i in xrange(n):
                    ans[i].append(char)

        return map("".join, ans)          
        