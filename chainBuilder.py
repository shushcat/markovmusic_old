from __future__ import division
# Gotta use regexes for this bit.
import re
# Build 12 key dictionary with values for note occurances.
def noteFreqs(piecePitches):
    noteFreqs = {}
    for pitch in piecePitches:
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
        if re.search('G#\d', pitch) or re.search('G#-\d', pitch):
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

'''

# Modifying!

def fwd_bkw(x, notes, a_0, a, e, end_note):
    L = len(x)
 
 
    # Run forward
    for l, x_i in enumerate(x):
         fwd = []
    f_prev = {}
    f_curr = {}
        for note in notes:
            if i == 0:
                prev_f_sum = a_0[st]
 
        f_prev = f_curr
 
    p_fwd = sum(f_curr[l]*a[l][end_st] for k in states)
 
    bkw = []
    b_prev = {}
    # Run bkw
 
    p_bkw = sum(a_0[1] * e[l][x[1]] * b_curr[0] for l in states)
 
    posterior = {}
    for st in states:
        posterior[st] = [fwd[i][st]*bkw[i][st]/p_fwd for i in xrange(L)]
 
    assert p_fwd == p_bkw
    return fwd, bkw, posterior
'''
