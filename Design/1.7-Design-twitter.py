#Time complexit O(followee) or O(k)
# space O(k) where k = no. of followee of a user
class Twitter:
    """
    similar to merging k sorted(linked-list) list question
    """
    def __init__(self):
        self.count = 0 #to keep track of tweet sequence no.
        self.followMap = defaultdict(set) # set so that we can unfollow in O(1) time
        self.tweetMap = defaultdict(list) # as we add in time sequence so list is fine
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # we append count with tweetId, as we need in when we try to get recent tweets
        self.tweetMap[userId].append([self.count, tweetId])
        # increment counter(max heap)
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        #Following oneself just to make this work
        self.followMap[userId].add(userId)
        # Add last tweets of all followee ie.end corners of k lists for all the followee + itself
        for followeeId in self.followMap[userId]: #O(followee)
            # check if there is some tweet of the followee
            if followeeId in self.tweetMap:
            # take index as we need it to insert elem just before it in tweetlist
                index = len(self.tweetMap[followeeId]) -1
                # read last tweet
                count, tweetId = self.tweetMap[followeeId][index]
            # adding followeeId and index as we need them to push next elem in heap
                maxHeap.append([count, tweetId, followeeId, index])
        heapq.heapify(maxHeap) #O(followee)
        
        # Removing latest tweet and adding just before tweet of same user
        while maxHeap and len(res) < 10: #o(10)
            count, tweetId, followeeId, index = heapq.heappop(maxHeap) #o(log(followee)
            res.append(tweetId)
            index -=1
            if index >= 0:
                # read tweet of same followee which was just before the above read tweet
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, [count, tweetId, followeeId, index]) #o(log(followee)
        return res
            
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId) 

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId) 
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)