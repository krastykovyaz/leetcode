# Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

# Users and tweets are uniquely identified by their IDs (integers).

# Implement the following methods:

# Twitter() Initializes the twitter object.
# void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
# List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.
# Example 1:

# Input:
tweets = ["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

# Output:
# [null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

# Input:
tweets = ["Twitter", "postTweet", [1, 100], "follow", [1, 1], "getNewsFeed", [1], "unfollow", [1, 1], "getNewsFeed", [1]]

# Output:
# [null,null,null,[100],null,[100]]

# Explanation:
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 10); # User 1 posts a new tweet with id = 10.
# twitter.postTweet(2, 20); # User 2 posts a new tweet with id = 20.
# twitter.getNewsFeed(1);   # User 1's news feed should only contain their own tweets -> [10].
# twitter.getNewsFeed(2);   # User 2's news feed should only contain their own tweets -> [20].
# twitter.follow(1, 2);     # User 1 follows user 2.
# twitter.getNewsFeed(1);   # User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
# twitter.getNewsFeed(2);   # User 2's news feed should still only contain their own tweets -> [20].
# twitter.unfollow(1, 2);   # User 1 unfollows user 2.
# twitter.getNewsFeed(1);   # User 1's news feed should only contain their own tweets -> [10].

from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = []
        self.users = defaultdict(set)
        self.followers = defaultdict(set)
        self.heap_tweets = []

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].add(tweetId)  
        self.heap_tweets.append((len(self.heap_tweets), tweetId))
   
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [(-hp[0], hp[1]) for hp in self.heap_tweets]
        followeers = self.followers[userId] | {userId}
        heapq.heapify(heap)
        out = []
        seen = set()
        while heap and len(out) < 10:
            _, twid = heapq.heappop(heap)
            for u in followeers:
                if twid in self.users[u] and twid not in seen:
                    seen.add(twid)
                    out.append(twid)
        return out

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].remove(followeeId)



if __name__=='__main__':
    twitter = Twitter()
    twitter.postTweet(1, 100)
    twitter.follow(1, 1)
    
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 1)
    # print(twitter.users)
    # print(twitter.followers)
    print(twitter.getNewsFeed(1))
    # twitter = Twitter()
    # twitter.postTweet(1, 10) # User 1 posts a new tweet with id = 10.
    # twitter.postTweet(2, 20) # User 2 posts a new tweet with id = 20.
    # print(twitter.getNewsFeed(1) )  # User 1's news feed should only contain their own tweets -> [10].
    # print(twitter.getNewsFeed(2)  ) # User 2's news feed should only contain their own tweets -> [20].
    # twitter.follow(1, 2)     # User 1 follows user 2.
    # print(twitter.getNewsFeed(1) )   # User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
    # print(twitter.getNewsFeed(2)  ) # User 2's news feed should still only contain their own tweets -> [20].
    # twitter.unfollow(1, 2)   # User 1 unfollows user 2.
    # print(twitter.getNewsFeed(1))   # User 1's news feed should only contain their own tweets -> [10].


        
