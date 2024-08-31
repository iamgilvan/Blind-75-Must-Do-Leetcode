from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.fallowMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int, feedLength=10) -> List[int]:
        res = [] # ordered starting from recent
        minHeap =[]
        self.fallowMap[userId].add(userId)
        for followerId in self.fallowMap[userId]:
            if followerId in self.tweetMap:
                idx = len(self.tweetMap[followerId]) - 1
                time , ttId = self.tweetMap[followerId][idx]
                minHeap.append([time, ttId, followerId, idx - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < feedLength:
            time, ttId, followerId, idx = heapq.heappop(minHeap)
            res.append(ttId)
            if idx >= 0:
                time , ttId = self.tweetMap[followerId][idx]
                heapq.heappush(minHeap, [time, ttId, followerId, idx - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fallowMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fallowMap[followerId].discard(followeeId)


twitter = Twitter();
twitter.postTweet(1, 5); # User 1 posts a new tweet (id = 5).
assert twitter.getNewsFeed(1) == [5]  # User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2)
twitter.postTweet(2, 6)
assert twitter.getNewsFeed(1) == [6, 5]  # User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2)  # User 1 unfollows user 2.
assert twitter.getNewsFeed(1) == [5]# User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.