# optimised solution to avoid extra dict lookup
def isValid(self, s: str) -> bool:
    dic = {'(':1 , ')':2 , '[':3 , ']':6 , '{':5 , '}':10}
    res = []
    for one in s:
        temp = dic[one]
        if(temp %2 ):
            res.append(temp)
        else:
            if(len(res) and res[-1]==temp//2):
                del res[-1]
            else:
                return False
    return res==[]

#  standard solution
# def isValid(self, s: str) -> bool:
        
#         closeToOpen = { ")": "(" ,  "}": "{", "]": "["}
#         stack = []
        
        
#         for c in s:
#             if c in closeToOpen:
#                 if stack and stack[-1] == closeToOpen[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
        
#         return True if not stack else False