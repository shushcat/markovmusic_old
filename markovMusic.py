#!/usr/bin/env python

# Required modules installed in Python
import sys
import os

# Modules in this directory
import corporaIO 
import chainBuilder
# import corpViz

# Pieces to be processed; relative to . or corpus.
pieceList = ['supplementary corpora/WTK1.mid']

'''
Remember! Command line args are in sys.argv[1], sys.argv[2] ... sys.argv[0] is the script name itself and can be ignored This'll be needed it we get far enough along to allow calling the program on paths from the command line instead of hard-coding pieces.
'''


n = 0
for piece in pieceList:

    pitchList = corporaIO.pitchList(piece)
    noteFreqs = chainBuilder.noteFreqs(pitchList)
    totalNotes = chainBuilder.totalNotes(noteFreqs)
    indProbs = chainBuilder.indProbs(noteFreqs)
#    depProbs = chainBuilder.depProb

    print '-'*64
    print pieceList[n]
    print '-'*64

# Make a dictionary of (transitions  : occurrances).
    transDict = {}
    noteNum = 0
    while noteNum < (totalNotes - 1):
        thisThat = pitchList[noteNum] + pitchList[noteNum + 1]
        nextNum = noteNum + 1
        while nextNum < (totalNotes - 2):
            if thisThat == pitchList[nextNum] + pitchList[nextNum + 1]:
                transDict[thisThat] = transDict.get(thisThat, 0) + 1
            nextNum = nextNum + 1
        noteNum = noteNum + 1
    chainBuilder.probTrans(transDict)
    print '\n'

#    print 'Frequency(occurrence) of each note:'
#    print noteFreqs
#    print '\n'
#    print 'Independent probability of each note:'
#    print indProbs
#    print '\n'
    print 'Total notes in piece: ' + str(totalNotes)
#    print '\n'
#    chainBuilder.thatThis(indProbs['A'], indProbs['B'])
#    print chainBuilder.probNext('A')
#    n = n + 1
