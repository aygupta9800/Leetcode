# soln 2
def lengthOfLastWord(self, s: str) -> int:
    l = 0
    for i in range(len(s) -1, -1, -1):
        if s[i] == ' ':
            if  l==0:
                continue
            else:
                return l
        else:
            l += 1
    return l
# soln 1
# def lengthOfLastWord(self, s: str) -> int:
#     arr = s.strip().split(" ")
#     return len(arr[-1])