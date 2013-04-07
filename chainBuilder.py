# Gotta use regexes for this bit.
import re
# Build 12 key dictionary with values for note occurances.
def pitchFreq(piecePitches):
    pitchFreqs = {}
    for pitch in piecePitches:
        if re.search('A.', pitch):
            pitchFreqs['A'] = pitchFreqs.get('A', 0) + 1
        if re.search('A#.', pitch):
            pitchFreqs['A#'] = pitchFreqs.get('A#', 0) + 1
        if re.search('B.', pitch):
            pitchFreqs['B'] = pitchFreqs.get('B', 0) + 1
        if re.search('C.', pitch):
            pitchFreqs['C'] = pitchFreqs.get('C', 0) + 1
        if re.search('C#.', pitch):
            pitchFreqs['C#'] = pitchFreqs.get('C#', 0) + 1
        if re.search('D.', pitch):
            pitchFreqs['D'] = pitchFreqs.get('D', 0) + 1
        if re.search('D#.', pitch):
            pitchFreqs['D#'] = pitchFreqs.get('D#', 0) + 1
        if re.search('E.', pitch):
            pitchFreqs['E'] = pitchFreqs.get('E', 0) + 1
        if re.search('F.', pitch):
            pitchFreqs['F'] = pitchFreqs.get('F', 0) + 1
        if re.search('F#.', pitch):
            pitchFreqs['F#'] = pitchFreqs.get('F#', 0) + 1
        if re.search('G.', pitch):
            pitchFreqs['G'] = pitchFreqs.get('G', 0) + 1
        if re.search('G#.', pitch):
            pitchFreqs['G#'] = pitchFreqs.get('G#', 0) + 1
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
'''
