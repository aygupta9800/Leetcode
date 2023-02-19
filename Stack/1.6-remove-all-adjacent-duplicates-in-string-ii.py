class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        """
        maintain stack with last value and its consecutive count as
        tuple value
        
        """
        
        stack = []
        
        for i in s:
            # print(stack)
            if stack and stack[-1][0] == i:
                    stack[-1][1] += 1
                    if stack[-1][1] == k:
                        stack.pop()
            else:
                stack.append([i, 1])
        # print(stack)
        return "".join(stack[i][1]*stack[i][0] for i in range(len(stack)))
                
                

        