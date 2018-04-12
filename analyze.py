from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
import json

bladeRunnerFilename = 'data/bladerunner.json'
blackPantherFN = 'data/blackpanther.json'
apesFN = 'data/apes.json'
lastJediFN = 'data/lastjedi.json'
legoBatmanFN = 'data/legobatman.json'

def analyzeText(filename):
    tweets_file = open(filename, "r")
    count = 0.0
    sum = 0.0
    for line in tweets_file:
        try:
            # Read in one line of the file, convert it into a json object 
            tweet = json.loads(line.strip())
            blob = TextBlob(tweet['text'])
            sum = blob.sentiment.polarity + sum
            count = count + 1.0

        except:
            # read in a line is not in JSON format (sometimes error occured)
            continue
    return sum/count

bladeRunner = analyzeText(bladeRunnerFilename)
blackPanther = analyzeText(blackPantherFN)
apes = analyzeText(apesFN)
lastJedi = analyzeText(lastJediFN)
legoBatman = analyzeText(legoBatmanFN)

print 'bladerunner:',bladeRunner
print 'black panther:',blackPanther
print 'apes:',apes
print 'last jedi:',lastJedi
print 'lego batman:',legoBatman

