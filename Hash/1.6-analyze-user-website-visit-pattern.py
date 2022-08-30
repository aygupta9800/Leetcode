
# The score of a pattern is the number of users that visited all the websites
#  in the pattern in the same order they appeared in the pattern.
# Q. Return the pattern with the largest score. If there is more than one pattern
#  with the same largest score, return the lexicographically smallest such pattern.

# Example 1:
# Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
# timestamp = [1,2,3,4,5,6,7,8,9,10],
# website = ["home","about","career","home","cart","maps","home","home","about","career"]

# Output: ["home","about","career"]
# Explanation: The tuples in this example are:
# ["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
# The pattern ("home", "about", "career") has score 2 (joe and mary).
# The pattern ("home", "cart", "maps") has score 1 (james).
# The pattern ("home", "cart", "home") has score 1 (james).
# The pattern ("home", "maps", "home") has score 1 (james).
# The pattern ("cart", "maps", "home") has score 1 (james).
# The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).



class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        users = defaultdict(list)
    
        for user, time, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])): 
            users[user].append(site)

        patterns = Counter()

        # 1. 3 sequence combinations of sites in order
        # 2. make set since duplicate pattern possible
        # 3. update the pattern hashmap with the Counter values of pattern
        for user, sites in users.items():
            patterns.update(Counter(set(combinations(sites, 3))))
        
        # to sort dict first lexicographically and then getting max first value
        return max(sorted(patterns), key=patterns.get)