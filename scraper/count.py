#!/usr/bin/python

import sys
import json

if __name__ == '__main__':
    with open(sys.argv[1]) as file:
        like = 0
        retweet = 0
        reply = 0
        data = json.load(file)
        #for tweet in data:
            #like = like + tweet['likes']
            #retweet = retweet + tweet['retweets']
            #reply = reply + tweet['replies']
    print("Likes: " + like)
    print("Retweets: " + retweet)
    print("Replies: " + reply)
