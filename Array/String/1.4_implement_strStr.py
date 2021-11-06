# Input: haystack = "hello", needle = "ll"
# Output: 2
# soln 1
def strStr(self, haystack: str, needle: str) -> int:
    l = len(needle)
    h = len(haystack)
    if l == 0:
        return 0
    if h < l:
        return -1
    for i in range(0, h - l + 1):
        if haystack[i: i+l] == needle:
            return i
    return -1
# def strStr(self, haystack: str, needle: str) -> int:
#     try:
#         index = haystack.index(needle)
#         return index
#     except:
#         return -1
        