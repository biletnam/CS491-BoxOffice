#!/usr/bin/python

import sys
import json
import datetime as dt
from twitterscraper import query_tweets

if __name__ == '__main__':
    print("Running...")
    tweet_list = query_tweets("Blade Runner 2049", None, dt.date(2017,10,2), dt.date(2017,10,7))
    print("Success!")
    with open('bladerunner.json','w') as out:
        out.write(str(len(tweet_list)))
        for tweet in tweet_list:
            data = {"text": tweet.text, "replies": tweet.replies, "retweets": tweet.retweets, "likes": tweet.likes}
            out.write('\n')
            json.dump(data,out)
