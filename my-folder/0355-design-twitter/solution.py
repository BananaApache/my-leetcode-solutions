class Twitter:

    def __init__(self):
        self.users = defaultdict(lambda: {'posts': [], 'following': set()}) # userId -> {posts: [], following: []}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId]['posts'].append( (self.time, tweetId) )
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        for following in self.users[userId]['following'] | {userId}:
            minHeap += self.users[following]['posts']
        
        heapq.heapify_max(minHeap)

        news = []
        k = 10
        while len(minHeap) > 0 and k > 0: # stop when (k is 0) OR (minHeap is empty)
            news.append(heapq.heappop_max(minHeap)[1])
            k -= 1

        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId]['following'].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId]['following'].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
