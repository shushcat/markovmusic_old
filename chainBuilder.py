# First, need to combine dictionary entries by note. 
def getFreqs(piecePitches):
    # Dictionary of overall note frequencies per piece.
    pitchFreqs = {}
    for piece in piecePitches:
        pitchFreqs[piece] = pitchFreqs.get(piece, 0) + 1
    return pitchFreqs

'''
Bayes' Theorem:
    P(x|y) = P(x)P(y|x)/P(y)
    To be used for generation of transition tables.
'''

# P of each note in each piece given the immediately preceding note.
# def probNext():

def noteProb(noteFreqs):
    # Dictionary of overall note probabilities per piece.
    total = float(len(noteFreqs))
    noteProbs = {}
    for notes, freqs in noteFreqs.items():
        noteProbs[notes] = freqs / total
    return noteProbs

# This needs to return a 12x12 matrix of note frequencies; a transition table for the particular piece.

'''

def sumFreqs(pitchFreqs):
    # Some kinda regular expression search here...
    if 'A\d'
    # elif 'A#'
    # elif 'B'
    # elif 'C'
    # elif 'C#'
    # elif 'D'
    # elif 'D#'
    # elif 'E'
    # elif 'F'
    # elif 'F#'
    # elif 'G'
    # elif 'G#'
'''
