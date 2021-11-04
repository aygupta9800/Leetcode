# Input: haystack = "hello", needle = "ll"
# Output: 2
# soln 1
def strStr(self, haystack: str, needle: str) -> int:
    l = len(needle)
    if l == 0:
        return 0
    for i in range(0, len(haystack) - l + 1):
        if haystack[i: i+l] == needle:
            return i
    return -1
# def strStr(self, haystack: str, needle: str) -> int:
#     try:
#         index = haystack.index(needle)
#         return index
#     except:
#         return -1
        