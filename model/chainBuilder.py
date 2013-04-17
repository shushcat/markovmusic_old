from __future__ import division
# Gotta use regexes for this bit.
import re

# Build 12 key dictionary with values for note occurances.
def getNoteFreqs(pitchList):
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

# Frequencies of transitions, collapsed to single octave.
def getTransFreqs(pitchList, totalNotes):
    transFreqs= {}
    noteNum = 0
    while (noteNum < (totalNotes - 1)):
        nextNum = noteNum + 1
        thisLink = re.sub(r'(.+)(\d)(.+)(\d)', r'\1\3', pitchList[noteNum] + pitchList[nextNum])
        transFreqs[thisLink] = transFreqs.get(thisLink, 0) + 1
        noteNum = noteNum + 1
    return transFreqs

# Total number of notes in a piece.
def getTotalNotes(noteFreqs):
    total = 0
    for freq in noteFreqs:
        total = total + noteFreqs.get(freq)
    return total

# Total transitions in a piece.
def getTotalTrans(transFreqs):
    total = 0
    for trans in transFreqs:
        total = total + transFreqs.get(trans)
    return total

# Independent p(note) per piece.
def getNoteProbs(noteFreqs):
    noteProbs = {}
    for pitch, freq in noteFreqs.items():
        noteProbs[pitch] = freq / getTotalNotes(noteFreqs)
    return noteProbs

# Dictionary of transition probabilities. Very small (< 0.002) value getting lost; fix later.
def getTransProbs(transFreqs, totalTrans):
    transProbs = {}
    for trans, freq in transFreqs.items():
        transProbs[trans] = freq / totalTrans
    return transProbs
