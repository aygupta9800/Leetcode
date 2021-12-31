# letter-combinations-of-a-phone-number
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []
        
        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(index, path):
            #checking base condn
            if len(path) == len(digits):
                combinations.append("".join(path))
                return # Backtrack
            
            # loop through the possible next letters
            possible_letters = letters[digits[index]]
            for L in possible_letters:
                # Add the letter to our current path
                path.append(L)
                # Move on to the next digit
                backtrack(index+1, path)
                # backtracking by removing the letter from path before moving to next
                path.pop()
            
        
        #initiate backtracking with empty path and start index 0
        combinations = []
        backtrack(0, [])
        return combinations

# Complexity Analysis
# Time complexity: O(4^N.N), where NN is the length of digits. Note that 4 in this expression is referring to the maximum value length in the hash map, and not to the length of the input.

# The worst-case is where the input consists of only 7s and 9s. In that case, we have to explore 4 additional paths for every extra digit. Then, for each combination, it costs up to NN to build the combination. This problem can be generalized to a scenario where numbers correspond with up to MM digits, in which case the time complexity would be O(M^N. N). For the problem constraints, we're given, M=4, because of digits 7 and 9 having 4 letters each.

# Space complexity: O(N), where NN is the length of digits.

# Not counting space used for the output, the extra space we use relative to input size is the space occupied by the recursion call stack. It will only go as deep as the number of digits in the input since whenever we reach that depth, we backtrack.

# As the hash map does not grow as the inputs grows, it occupies O(1) space.

