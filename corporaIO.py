from music21 import *
from music21 import corpus
t 

# loads supported files into music21 streams; music21.stream.Score objects?
music21.converter
def addFile(file):

streamObject = converter.parse(humdrum.testFiles.mazurka6)
stream2 = streamObject.stripTies()
correlated = graph.Plot3DBarsPitchSpaceQuarterLength(stream2.flat)
correlated.process() 

catalog = stream.Score()
for work in corpus.beethovenStringQuartets():
    if work.flat.getElementsByClass(meter.TimeSignature)[0].ratioString == '6/8':
        catalog.append(work.measureRange(0,2))
catalog.show() 

# return something interpretable by chainBuilder
