class Twitter:

    def __init__(self):
        self.usersFollowings = {} # userID -> set() of following IDs
        self.userTweets = {} # userID -> Array[(time, tweetID)]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.userTweets[userId] = self.userTweets.get(userId, []) + [(self.time, tweetId)]
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        followingIds = list(self.usersFollowings.get(userId, set()))
        followingIds.append(userId)

        pointers = []
        sumPointers = 0
        for followingId in followingIds:
            if followingId in self.userTweets:
                pointers.append(len(self.userTweets[followingId]))
                sumPointers += len(self.userTweets[followingId])
            else:
                pointers.append(0)

        # stop when length of result >= 10 OR if all pointers at 0
        while len(result) < 10 and sumPointers > 0:
            mostRecent = (-1, None)
            lastMoved = -1

            index = 0
            for followingId in followingIds:
                if pointers[index] > 0:
                    tweet = self.userTweets[followingId][pointers[index] - 1]
                    if tweet[0] > mostRecent[0]:
                        lastMoved = index
                        mostRecent = tweet
                    
                index += 1

            if lastMoved != -1:
                pointers[lastMoved] -= 1
                sumPointers -= 1
                result.append(mostRecent[1])
            else:
                break

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.usersFollowings:
            self.usersFollowings[followerId].add(followeeId)
        else:
            self.usersFollowings[followerId] = set({followeeId})

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.usersFollowings:
            self.usersFollowings[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
