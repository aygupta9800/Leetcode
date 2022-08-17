# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.



# Example 1:
# Input: s = "aab"
# Output: "aba"

# Example 2:
# Input: s = "aaab"
# Output: ""

# time complexity: O(nlogk) where n total alphabets, k unique alphbets, space: O(k)=> unique alphabets
class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Its similar to task schedular question, just that we can place each char after 1 distance.
        we can simply use prev variable to track variable which is on hold rather than need to use deque like in other question
        """
        count = Counter(s)
        #keeping each unique char in heap and than poping based on freq from
        # whatever char is avail to pick
        maxHeap = [ [-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap) #o(n)
        prev = None
        res = []
        #O(n)
        while maxHeap or prev:
            #If invalid case where nthing is avail to pick at some pos
            if prev and not maxHeap:
                return ""
            #o(logn)=> logk that is k is no. of unique char
            cnt, char = heapq.heappop(maxHeap)
            res.append(char)
            # decrement cnt of char
            cnt += 1
            #Use Prev of before iteration and add it to heap
            if prev:
                #o(logn) => logk that is k is no. of unique char
                heapq.heappush(maxHeap, prev)
                prev = None
            # Add currently used char to prev if still cnt remaining
            if cnt:
                prev = [cnt, char]
        return "".join(res)