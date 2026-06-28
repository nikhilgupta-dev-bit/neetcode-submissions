import heapq
from collections import defaultdict
from typing import List

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)   # userId -> [(time, tweetId)]
        self.following = defaultdict(set) # userId -> set()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []

        # user should follow themselves
        self.following[userId].add(userId)

        for user in self.following[userId]:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(min_heap, (time, tweetId))
                
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)

        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])

        return res[::-1]  # most recent first

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
