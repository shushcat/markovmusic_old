from music21 import *
from music21 import corpus

def thatone():
    print "It\'s a doin\' that!"

streamObject = converter.parse(humdrum.testFiles.mazurka6)
stream2 = streamObject.stripTies()
correlated = graph.Plot3DBarsPitchSpaceQuarterLength(stream2.flat)
correlated.process() 

catalog = stream.Score()
for work in corpus.beethovenStringQuartets():
    if work.flat.getElementsByClass(meter.TimeSignature)[0].ratioString == '6/8':
        catalog.append(work.measureRange(0,2))
catalog.show() 
