from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
import json

bladeRunnerFilename = 'data/bladerunner.json'
blackPantherFN = 'data/blackpanther.json'
apesFN = 'data/apes.json'
lastJediFN = 'data/lastjedi.json'
legoBatmanFN = 'data/legobatman.json'
dunkirkFN = 'data/dunkirk.json'
getoutFN = 'data/getout.json'
guardiansFN = 'data/guardians.json'
thorFN = 'data/thor.json'
waterFN = 'data/water.json'
wonderFN = 'data/wonder.json'
arthurFN = 'data/arthur.json'
baywatchFN = 'data/baywatch.json'
beautyFN = 'data/beauty.json'
justiceFN = 'data/justice.json'

def analyzeText(filename):
    tweets_file = open(filename, "r")
    count = 0.0
    sum = 0.0
    positiveCount = 0
    negativeCount = 0
    neutralCount = 0
    for line in tweets_file:
        try:
            # Read in one line of the file, convert it into a json object 
            tweet = json.loads(line.strip())
            blob = TextBlob(tweet['text'])
            sum = blob.sentiment.polarity + sum
            count = count + 1.0
            if blob.sentiment.polarity > 0:
                positiveCount = positiveCount + 1
            elif blob.sentiment.polarity == 0:
                neutralCount = neutralCount + 1
            else:
                negativeCount = negativeCount + 1

        except:
            # read in a line is not in JSON format (sometimes error occured)
            continue
    return sum/count,positiveCount,negativeCount,neutralCount

bladeRunner = analyzeText(bladeRunnerFilename)
blackPanther = analyzeText(blackPantherFN)
apes = analyzeText(apesFN)
lastJedi = analyzeText(lastJediFN)
legoBatman = analyzeText(legoBatmanFN)
arthur = analyzeText(arthurFN)
baywatch = analyzeText(baywatchFN)
beauty = analyzeText(beautyFN)
dunkirk = analyzeText(dunkirkFN)
getout = analyzeText(getoutFN)
guardians = analyzeText(guardiansFN)
justice = analyzeText(justiceFN)
thor = analyzeText(thorFN)
water = analyzeText(waterFN)
wonder = analyzeText(wonderFN)

print 'bladerunner:',bladeRunner[0],bladeRunner[1],bladeRunner[2],bladeRunner[3]
print 'black panther:',blackPanther[0],blackPanther[1],blackPanther[2],blackPanther[3]
print 'apes:',apes[0],apes[1],apes[2],apes[3]
print 'last jedi:',lastJedi[0],lastJedi[1],lastJedi[2],lastJedi[3]
print 'lego batman:',legoBatman[0],legoBatman[1],legoBatman[2],legoBatman[3]
print 'arthur:',arthur[0],arthur[1],arthur[2],arthur[3]
print 'baywatch:',baywatch[0],baywatch[1],baywatch[2],baywatch[3]
print 'beauty:',beauty[0],beauty[1],beauty[2],beauty[3]
print 'dunkirk:',dunkirk[0],dunkirk[1],dunkirk[2],dunkirk[3]
print 'getout:',getout[0],getout[1],getout[2],getout[3]
print 'guardians:',guardians[0],guardians[1],guardians[2],guardians[3]
print 'justice:',justice[0],justice[1],justice[2],justice[3]
print 'thor:',thor[0],thor[1],thor[2],thor[3]
print 'water:',water[0],water[1],water[2],water[3]
print 'wonder:',wonder[0],wonder[1],wonder[2],wonder[3]

