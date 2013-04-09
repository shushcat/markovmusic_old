#!/usr/bin/env python

# Required modules installed in Python
import sys
import os

# Modules in this directory
from corporaIO import pitchList 
from chainBuilder import *
# import corpViz

# Pieces to be processed; relative to . or corpus.
pieceList = ['supplementary corpora/WTK1.mid']

'''
Remember! Command line args are in sys.argv[1], sys.argv[2] ... sys.argv[0] is the script name itself and can be ignored This'll be needed if we get far enough along to allow calling the program on paths from the command line instead of hard-coding pieces.
'''


n = 0
for piece in pieceList:
    pitchList = pitchList(piece)
    noteFreqs = noteFreqs(pitchList)
    totalNotes = totalNotes(noteFreqs)
    transFreqs = transFreqs(pitchList, totalNotes)
    indProbs = indProbs(noteFreqs)
    totalTrans = totalTrans(transFreqs)
    transProbs = transProbs(transFreqs, totalNotes)

#    print '-'*64
#    print pieceList[n]
#    print '-'*64
    print '\n'
#    for pitch in pitchList:
#        print pitch

# Make a dictionary of (transitions  : occurrances).
    #print transProbs(transFreqs, totalTrans)

#    print 'Frequency(occurrence) of each note:'
#    print noteFreqs
#    print '\n'
#    print 'Independent probability of each note:'
#    print indProbs
#    print '\n'
#    print 'Total notes in piece: ' + str(totalNotes)
#    print '\n'
#    chainBuilder.thatThis(indProbs['A'], indProbs['B'])
#    print chainBuilder.probNext('A')
    n = n + 1
