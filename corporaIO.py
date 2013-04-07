from music21 import *
from music21 import corpus

'Accepts paths to supported filetypes and returns a list of pitches and their frequencies.'

# Makes music21.stream.Score objects
def addPiece(piece):
    # Parses and flattens so notes can be linearly compared. Flattening precedence is: offset time, priority (low to high?), classSortOrder and takes place automatically when applying the str() method.
    added = converter.parseFile(piece)
    piecePitches = [str(p) for p in added.pitches]
    pitchFreqs = getFreqs(piecePitches)
    return pitchFreqs 


def getFreqs(piecePitches):
    # Dictionary of overall note frequencies per piece.
    pitchFreqs = {}
    for piece in piecePitches:
        pitchFreqs[piece] = pitchFreqs.get(piece, 0) + 1
    return pitchFreqs

# My precious hysteriograms
# streamObject = converter.parse(humdrum.testFiles.piece)
# stream2 = streamObject.stripTies()
# correlated = graph.Plot3DBarsPitchSpaceQuarterLength(stream2.flat)
# correlated.process() 
