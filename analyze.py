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

        except:
            # read in a line is not in JSON format (sometimes error occured)
            continue
    return sum/count

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

print 'bladerunner:',bladeRunner
print 'black panther:',blackPanther
print 'apes:',apes
print 'last jedi:',lastJedi
print 'lego batman:',legoBatman
print 'arthur:',arthur
print 'baywatch:',baywatch
print 'beauty:',beauty
print 'dunkirk:',dunkirk
print 'getout:',getout
print 'guardians:',guardians
print 'justice:',justice
print 'thor:',thor
print 'water:',water
print 'wonder:',wonder

