#Approach 2
# Algorithm

# The trick is to count the elements of T. After we have some count[char] = (the number of occurrences of char in T), we can write these elements in the order we want. The order is S + (characters not in S in any order).
# For more details on the algorithm, please see the inlined comments in each implementation.
# Approach 2:
class Solution:
    def customSortString(self, order: str, s: str) -> str:
# count[char] will be the number of occurrences of
        # 'char' in s.
        count = collections.Counter(s)
        ans = []

        # Write all characters that occur in order, in the order of order.
        for c in order:
            ans.append(c * count[c])
            # Set count[c] = 0 to denote that we do not need
            # to write 'c' to our answer anymore.
            count[c] = 0

        # Write all remaining characters that don't occur in S.
        # That information is specified by 'count'.
        for c in count:
            ans.append(c * count[c])

        return "".join(ans)

#Approach 1: putting string in its res order pos in array of 26 char
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        orderMap = { n : i  for i, n in enumerate(order)}
        temp = ""
        res = [""]* len(order)
        for i in range(len(s)):
            if s[i] not in orderMap:
                temp += s[i]
            else:
                res[orderMap[s[i]]] += s[i]
        for i in range(len(order)):
            if res[i] != "":
                temp += res[i]
        return temp