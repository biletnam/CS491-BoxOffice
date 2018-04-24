#!/usr/bin/python
#Run the program with $python scraper.py string int int int int int int string
#Command line args are:
##1. Keyword (ex. "the last jedi")
##2. Start Year (ex. 2017)
##3. Start Month (ex. 5)
##4. Start Day (ex. 27)
##5. End Year
##6. End Month
##7. End Day
##8. Output file name (ex. "starwars.json")

import sys
import json
import datetime as dt
from twitterscraper import query_tweets

if __name__ == '__main__':
    print("Running...")
    tweet_list = query_tweets(sys.argv[1], None, dt.date(int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4])), dt.date(int(sys.argv[5]),int(sys.argv[6]),int(sys.argv[7])))
    print("Success!")
    with open(sys.argv[8],'w') as out:
        out.write(str(len(tweet_list)))
        for tweet in tweet_list:
            data = {"text": tweet.text, "replies": tweet.replies, "retweets": tweet.retweets, "likes": tweet.likes}
            out.write('\n')
            json.dump(data,out)
