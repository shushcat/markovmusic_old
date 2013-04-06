from music21 import *
from music21 import corpus

# Makes music21.stream.Score objects
def addPiece(piece):
    # Parses and flattens so notes can be linearly compared. Flattening precedence is: offset time, priority (low to high?), classSortOrder
    added = converter.parseFile(piece)
    piecePitches = [str(p) for p in added.pitches]
    return piecePitches

# This needs to return a 12x12 matrix of note frequencies; a transition table for the particular piece.

# My hysteriograms
# streamObject = converter.parse(humdrum.testFiles.mazurka6)
# stream2 = streamObject.stripTies()
# correlated = graph.Plot3DBarsPitchSpaceQuarterLength(stream2.flat)
# correlated.process() 

'''
catalog = stream.Score()
for work in corpus():
    if work.flat.getElementsByClass(meter.TimeSignature)[0].ratioString == '6/8':
        catalog.append(work.measureRange(0,2))
catalog.show() 
'''

# return something interpretable by chainBuilder
