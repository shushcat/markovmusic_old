from __future__ import division
# Gotta use regexes for this bit.
import re
# For working with matrices.
import numpy
from collections import Counter

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

# There may be a problem here :-?
# Frequencies of transitions, collapsed to single octave.
def transFreqs(pitchList, totalNotes):
    transDict = {}
    noteNum = 0
    while noteNum < (totalNotes - 1):
        thisThat = re.sub(r'(.+)(\d)(.+)(\d)', r'\1\3', pitchList[noteNum] + pitchList[noteNum + 1])
        nextNum = noteNum + 1
        while nextNum < (totalNotes - 2):
            if re.search(thisThat, re.sub(r'(.+)(\d)(.+)(\d)', r'\1\3', pitchList[nextNum] + pitchList[nextNum + 1])):
                transDict[thisThat] = transDict.get(thisThat, 0) + 1
            nextNum = nextNum + 1
        noteNum = noteNum + 1
    return transDict

# Total number of notes in a piece.
def totalNotes(noteFreqs):
    total = 0
    for freq in noteFreqs:
        total = total + noteFreqs.get(freq)
    return total

# Total transitions in a piece.
def totalTrans(transFreqs):
    total = 0
    for trans in transFreqs:
        total = total + transFreqs.get(trans)
    return total

# Independent p(note) per piece.
def indProbs(noteFreqs):
    indProbs = {}
    for pitch, freq in noteFreqs.items():
        indProbs[pitch] = freq / totalNotes(noteFreqs)
    return indProbs

# Dictionary of transition probabilities.
def transProbs(transFreqs, totalTrans):
    transProbs = {}
    for trans, freq in transFreqs.items():
        transProbs[trans] = freq / totalTrans
    return transProbs

    #transitions = numpy.arrange(1, 12)
    #print transitions
    totalTrans = 0
    totalProb = 0
#        totalTrans = totalTrans + transDict[trans]
#        print totalTrans
#        totalProb = totalProb + transDict[trans]/totalTrans

'''
Bayes' Theorem:
    P(x|y) = P(x)P(y|x)/P(y)
    To be used for generation of transition tables.

    Translated:
    P(next | preceding) = P(next)P(preceding | next)/P(preceding)
'''
