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
    notes = corporaIO.pitchList(piece)
    print '-'*64
    print pieceList[n]
    print '-'*64
    noteNum = 0
#    for note in notes:
#        print str(note[noteNum]) + ' is followed by ' + str(note[noteNum + 1])
    print 'Frequency(occurrence) of each note:'
    print chainBuilder.noteFreqs(notes)
    print '\n'
    print 'Independent probability of each note:'
    print chainBuilder.noteProb(chainBuilder.noteFreqs(notes))
    print '\n'
    print 'Total notes in piece: ' + str(chainBuilder.totalNotes(chainBuilder.noteFreqs(notes)))
    print '\n'
    n = n + 1
    print chainBuilder.totalNotes(chainBuilder.noteFreqs(notes))
    for note in notes:
        print note
