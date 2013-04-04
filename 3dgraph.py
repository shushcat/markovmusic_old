from music21 import *
streamObject = converter.parse(humdrum.testFiles.mazurka6)
stream2 = streamObject.stripTies()
correlated = graph.Plot3DBarsPitchSpaceQuarterLength(stream2.flat)
correlated.process() 
