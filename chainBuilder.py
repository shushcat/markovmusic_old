from __future__ import division
# Gotta use regexes for this bit.
import re

# Build 12 key dictionary with values for note occurances.
def noteFreqs(pitchList):
    noteFreqs = {}
    for pitch in pitchList:
        if re.search('A\d', pitch) or re.search('A-\d', pitch):
            noteFreqs['A'] = noteFreqs.get('A', 0) + 1
        if re.search('A#\d', pitch) or re.search('A#-\d', pitch):
            noteFreqs['A#'] = noteFreqs.get('A#', 0) + 1
        if re.search('B\d', pitch) or re.search('B-\d', pitch):
            noteFreqs['B'] = noteFreqs.get('B', 0) + 1
        if re.search('C\d', pitch) or re.search('C-\d', pitch):
            noteFreqs['C'] = noteFreqs.get('C', 0) + 1
        if re.search('C#\d', pitch) or re.search('C#-\d', pitch):
            noteFreqs['C#'] = noteFreqs.get('C#', 0) + 1
        if re.search('D\d', pitch) or re.search('D-\d', pitch):
            noteFreqs['D'] = noteFreqs.get('D', 0) + 1
        if re.search('D#\d', pitch) or re.search('D#-\d', pitch):
            noteFreqs['D#'] = noteFreqs.get('D#', 0) + 1
        if re.search('E\d', pitch) or re.search('E-\d', pitch):
            noteFreqs['E'] = noteFreqs.get('E', 0) + 1
        if re.search('F\d', pitch) or re.search('F-\d', pitch):
            noteFreqs['F'] = noteFreqs.get('F', 0) + 1
        if re.search('F#\d', pitch) or re.search('F#-\d', pitch):
            noteFreqs['F#'] = noteFreqs.get('F#', 0) + 1
        if re.search('G\d', pitch) or re.search('G-\d', pitch):
            noteFreqs['G'] = noteFreqs.get('G', 0) + 1
        if re.search('G#\d', pitch) or re.search('C-\d', pitch):
            noteFreqs['G#'] = noteFreqs.get('G#', 0) + 1
    return noteFreqs

# Total number of notes in a piece.
def totalNotes(noteFreqs):
    total = 0
    for freq in noteFreqs:
        total = total + noteFreqs.get(freq)
    return total

# Independent p(note) per piece.
def indProbs(noteFreqs):
    indProbs = {}
    for pitch, freq in noteFreqs.items():
        indProbs[pitch] = freq / totalNotes(noteFreqs)
    return indProbs

# Accepts two independent probabilities and returns probThat given probThis.
def thatThis(probThat, probThis, probThisThat):
    probThatThis = (probThat * probThisThat)/probThis
    print probThat
    print probThis

def depProb(transDict):
    depProb

# This needs to return a 12x12 matrix of note frequencies; a transition table for the particular piece. Best implemented as a 144 key dictionary.

'''
Bayes' Theorem:
    P(x|y) = P(x)P(y|x)/P(y)
    To be used for generation of transition tables.

    Translated:
    P(next | preceding) = P(next)P(preceding | next)/P(preceding)

    Forward-backward algorithm is the way to go, really, but can be deferred for now since that would be overreaching current project scope.
'''
