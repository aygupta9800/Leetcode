# Approach1 Stack and No String Reversal
# By associating the sign
# TIme : O(n), space:O(n)
class Solution:
    def calculate(self, s: str) -> int:
        #1. Apporach1 String reversal and calculation of subexpression
        #2 associate sign with the number
        stack = []
        operand = 0 # current digit
        res = 0 #for ongoing result
        sign = 1 #1 means +, -1 means negative
        
        for ch in s:
            if ch.isdigit():
                operand = (operand * 10) + int(ch)
                
            elif ch == "+":
            
                #evaluate the expression to the left, with result, sign, operand
                res += sign * operand
                # save the sign
                sign = 1
                
                # reset operand
                operand = 0
                
            elif ch == "-":
                res += sign * operand
                sign = -1
                operand = 0
                
            elif ch == "(":
                #push the result and sign on to the stack, for later
                # We push the result first, then sign
                stack.append(res)
                stack.append(sign)
                
                # reset operand , res , as if new eval begins for new subexpression
                sign = 1
                operand = 0 # no need as before opening there must be a closing bracket where we set operand to 0
                res = 0
            elif ch == ')':
                # evaluate the expression to the left with result, sign, operand
                res += sign * operand
                res *= stack.pop() # stack pop 1, sign
                res += stack.pop() # stack pop2, operand
                
                # reset the operand
                operand = 0
        return res +sign * operand
            
            