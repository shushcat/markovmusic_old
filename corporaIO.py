from music21 import *
from music21 import corpus

# Makes music21.stream.Score objects
def addPiece(piece):
    # Parses and flattens so notes can be linearly compared. Flattening precedence is: offset time, priority (low to high?), classSortOrder
    added = converter.parseFile(piece)
    piecePitches = [str(p) for p in added.pitches]
    baseFreq = noteFreq(piecePitches)
    baseProb = noteProb(baseFreq)
    return baseProb


def noteFreq(piecePitches):
    # Dictionary of overall note frequencies per piece.
    noteFreqs = {}
    for piece in piecePitches:
        noteFreqs[piece] = noteFreqs.get(piece, 0) + 1
    return noteFreqs

def noteProb(noteFreqs):
    # Dictionary of overall note probabilities per piece.
    total = float(len(noteFreqs))
    noteProbs = {}
    for notes, freqs in noteFreqs.items():
        noteProbs[notes] = freqs / total
    return noteProbs

# This needs to return a 12x12 matrix of note frequencies; a transition table for the particular piece.

# My hysteriograms
# streamObject = converter.parse(humdrum.testFiles.mazurka6)
# stream2 = streamObject.stripTies()
# correlated = graph.Plot3DBarsPitchSpaceQuarterLength(stream2.flat)
# correlated.process() 

# return something interpretable by chainBuilder
