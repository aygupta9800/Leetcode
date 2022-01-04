# 227. Basic Calculator II Medium

# Given a string s which represents an expression, evaluate this expression and return its value. 
# The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        """
        Algorithm

        Scan the input string s from left to right and evaluate the expressions based on the following rules
        1. If the current character is a digit 0-9 ( operand ), add it to the number currentNumber.
        2. Otherwise, the current character must be an operation (+,-,*, /). Evaluate the expression based on the type of operation.
        3. Addition (+) or Subtraction (-): We must evaluate the expression later based on the next operation. So, we must store the currentNumber to be used later. Let's push the currentNumber in the Stack.
        4. Multiplication (*) or Division (/): Pop the top values from the stack and evaluate the current expression. Push the evaluated value back to the stack.
        Once the string is scanned, pop from the stack and add to the result.
        """
        stack = []
        currentNum = 0
        operation = "+"
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                currentNum = currentNum * 10 + ord(ch) -ord('0')
            if (not ch.isdigit() and ch != " ") or i == len(s) -1:
                if operation == '-':
                    stack.append(-currentNum)
                elif operation == "+":
                    stack.append(currentNum)
                elif operation == "*":
                    stack.append(stack.pop() * currentNum)
                elif operation == "/":
                    # print("1:",stack)
                    num = stack.pop()
                    if num >= 0:
                        stack.append(num // currentNum)
                    else:
                        stack.append(-1* (-num //currentNum))
                    print("2:",stack)
                operation = ch
                currentNum = 0
        res = 0
        while len(stack) != 0:
            res += stack.pop()
        return res
        
 


