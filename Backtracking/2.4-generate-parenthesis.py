Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        """
        Add a bracket if it makes a valid sequence till that pos
        by hacing opn and close bracket count such that
        '(' can be inserted if opn < n and
        ')' can be inserted if opn >close
        """
        
        def backtrack(comb, opn, cl):
            if len(comb) == 2*n:
                res.append("".join(comb))
                return
            if opn < n:
                comb.append("(")
                backtrack(comb, opn +1, cl)
                comb.pop()
            if opn > cl:
                comb.append(")")
                backtrack(comb, opn, cl +1)
                comb.pop()
        backtrack([], 0, 0)
        return res