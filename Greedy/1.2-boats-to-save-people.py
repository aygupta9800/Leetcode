# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)class Solution:
def numRescueBoats(self, people: List[int], limit: int) -> int:
    people.sort()
    i, j = 0, len(people) -1
    
    ans = 0
    while i <= j:
        if people[i] + people[j] <= limit:
            i +=1
        j -= 1
        ans +=1
    return ans