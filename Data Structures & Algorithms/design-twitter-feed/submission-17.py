from collections import defaultdict
class Twitter:
    def __init__(self):
        self.users = defaultdict(list) # Keys users , values following
        self.posts = defaultdict(list) # Keys users, values post ids
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.posts[userId].append([tweetId, self.timestamp])

    def getNewsFeed(self, userId: int) -> List[int]:
        users_to_check = [userId] + self.users[userId]
        posts = []
        for u in users_to_check:
            posts.extend(self.posts[u])
        return [tid for tid, _ in heapq.nlargest(10, posts, key=lambda x: x[1])]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users[followerId] and followerId != followeeId:
            self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
