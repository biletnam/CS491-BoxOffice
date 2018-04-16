#!/usr/bin/python

import sys
import json

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        like = 0
        retweet = 0
        reply = 0
        next(file)
        for line in file:
            tweet = json.loads(line)
            like = like + int(tweet['likes'])
            retweet = retweet + int(tweet['retweets'])
            reply = reply + int(tweet['replies'])
    print("Likes: " + str(like))
    print("Retweets: " + str(retweet))
    print("Replies: " + str(reply))
