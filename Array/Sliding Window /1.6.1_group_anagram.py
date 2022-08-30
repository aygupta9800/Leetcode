
# Approach2
# Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.

# Algorithm

# We can transform each string s into a character count, count, consisting of 26 non-negative integers representing the 
# number of a's, b's, c's, etc. We use these counts as the basis for our hash map.
# Time complexity O(N.k) where n = total strings and k is max len of string
class Solution:
    def groupAnagrams(strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()



from collections import defaultdict
# compare by sorted string
# Time O(NKlogk)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
#             No need to check if not in dic as default will be []
            ans[str(sorted(s))].append(s)
        return ans.values()



    

# my soln
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs== [""]:
            return [[""]]
        dic = {}
        for i in range(0, len(strs)):
            arr = []
            sorted_str = "".join(sorted(strs[i])) #equal to str(sorted(strs[i]))
            if sorted_str in dic:
                dic[sorted_str].append(strs[i])
            else:
                arr.append(strs[i])
                dic[sorted_str]= arr
        # for key in dic:
        #     res.append(dic[key])
        # return res
        return dic.values()