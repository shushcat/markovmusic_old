from __future__ import division
# Gotta use regexes for this bit.
import re
# Build 12 key dictionary with values for note occurances.
def noteFreq(piecePitches):
    noteFreqs = {}
    for pitch in piecePitches:
        if re.search('A.', pitch):
            noteFreqs['A'] = noteFreqs.get('A', 0) + 1
        if re.search('A#.', pitch):
            noteFreqs['A#'] = noteFreqs.get('A#', 0) + 1
        if re.search('B.', pitch):
            noteFreqs['B'] = noteFreqs.get('B', 0) + 1
        if re.search('C.', pitch):
            noteFreqs['C'] = noteFreqs.get('C', 0) + 1
        if re.search('C#.', pitch):
            noteFreqs['C#'] = noteFreqs.get('C#', 0) + 1
        if re.search('D.', pitch):
            noteFreqs['D'] = noteFreqs.get('D', 0) + 1
        if re.search('D#.', pitch):
            noteFreqs['D#'] = noteFreqs.get('D#', 0) + 1
        if re.search('E.', pitch):
            noteFreqs['E'] = noteFreqs.get('E', 0) + 1
        if re.search('F.', pitch):
            noteFreqs['F'] = noteFreqs.get('F', 0) + 1
        if re.search('F#.', pitch):
            noteFreqs['F#'] = noteFreqs.get('F#', 0) + 1
        if re.search('G.', pitch):
            noteFreqs['G'] = noteFreqs.get('G', 0) + 1
        if re.search('G#.', pitch):
            noteFreqs['G#'] = noteFreqs.get('G#', 0) + 1
    return noteFreqs

# Total number of notes in a piece.
def totalNotes(noteFreqs):
    total = 0
    for freq in noteFreqs:
        total = total + noteFreqs.get(freq)
    return total

# Independent p(note).
def noteProb(noteFreqs):
    noteProbs = {}
    for pitch, freq in noteFreqs.items():
        noteProbs[pitch] = freq / totalNotes(noteFreqs)
    return noteProbs

# P of each note in each piece given the immediately preceding note.
def probNext():
    print 'wuttup'

# This needs to return a 12x12 matrix of note frequencies; a transition table for the particular piece. Best implemented as a 144 key dictionary.

'''
Bayes' Theorem:
    P(x|y) = P(x)P(y|x)/P(y)
    To be used for generation of transition tables.
'''
