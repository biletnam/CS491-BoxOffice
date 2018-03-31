#!/usr/bin/python

import sys
import json
import datetime as dt
from twitterscraper import query_tweets

if __name__ == '__main__':
    count = 0
    with open('output.json','w') as out:
        for tweet in query_tweets("Black Panther OR blackpanther", None, dt.date(2018,2,14), dt.date(2018,2,16)):
            data = {"text": tweet.text, "replies": tweet.replies, "retweets": tweet.retweets, "likes": tweet.likes}
            out.write('\n')
            json.dump(data,out)

