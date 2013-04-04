from music21 import *
streamObject = converter.parse('bach.bwv1.6.mxl')
stream2 = streamObject.stripTies()
correlated = graph.Plot3DBarsPitchSpaceQuarterLength(stream2.flat)
correlated.process() 
