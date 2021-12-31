# Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.
# Return all the possible results. You may return the answer in any order.


# Time Complexity : O(2^N)The optimization that we have performed is simply a better form of pruning. Pruning here is something that will vary from one test case to another. In the worst case, we can have something like ((((((((( and the left_rem = len(S) and in such a case we can discard all of the characters because all are misplaced. So, in the worst case we still have 2 options per parenthesis and that gives us a complexity of O(2^N).
# Space Complexity : The space complexity remains the same i.e. O(N)O(N) as previous solution. We have to go to a maximum recursion depth of NN before hitting the base case. Note that we are not considering the space required to store the valid expressions. We only count the intermediate space here.
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def getMinParenToRemove(s: str):
            minParenToRemove = 0
            openBr = 0
            for c in s:
                if c == "(":
                    openBr += 1
                elif c == ")":
                    if openBr == 0:
                        minParenToRemove += 1
                    else:
                        openBr -= 1
            minParenToRemove += openBr
            return minParenToRemove 
    
        def dfs(s, index, parenRemoveCount, openBr, path):
            if index == n:
                if parenRemoveCount == 0 and openBr == 0:
                    result.add(path)
                return
            
            if parenRemoveCount < 0:
                return
            
            if s[index] == "(":
                dfs(s, index+1, parenRemoveCount, openBr +1, path + "(")
                dfs(s, index+1, parenRemoveCount -1, openBr, path)
            elif s[index] == ")":
                if openBr > 0:
                    dfs(s, index+1, parenRemoveCount, openBr -1, path+ ")")
                dfs(s, index +1, parenRemoveCount -1, openBr, path)
            else:
                dfs(s, index+1, parenRemoveCount, openBr, path+s[index])
        
        minParenToRemoveCount = getMinParenToRemove(s)
        n = len(s)
        result = set()
        dfs(s, 0, minParenToRemoveCount, 0, "" )
        return list(result)
        