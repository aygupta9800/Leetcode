# Time complexity: O(N).

# We iterate over the given array once.
# Each building's index can be pushed to answer and popped from answer at most once, and both of the operations take O(1) time.
# Space complexity: O(N)O(N).

# There is no auxiliary space used other than the output. The output does not count towards the space complexity. However, in the worst-case scenario, answer may contain as many as N−1 indices, and then the very last building is the tallest, so the output will reduce to one index. In this scenario, the algorithm must store N−1 elements at some point, but only 1 element is included in the output.
# In Java, in order to maintain a dynamic size array, we created an extra Array List that supports fast O(1)O(1) push/pop operation. Array List can contain at most NN elements. Hence in Java, an additional O(N)O(N) space is used.

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        clearly a stack question
        """
        stack = []
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[-1]] <= heights[i]:
                stack.pop()
            stack.append(i)
            
        return stack
        