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
        # TODO: Can use heap also
        users_to_check = [userId]+self.users[userId]
        posts = []
        for u in users_to_check:
            posts = posts + self.posts[u]
        posts = sorted(posts, reverse=True, key=lambda item: item[1])
        return [item[0] for item in posts][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.users[followerId] and followerId != followeeId:
            self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
