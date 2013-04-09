#!/usr/bin/env python

# Required modules installed in Python
import sys
import os
import math

# Modules in this directory
from corporaIO import pitchList 
from chainBuilder import *
# import corpViz

# Pieces to be processed; relative to . or corpus
pieceList = ['supplementary corpora/WTK1.mid']

'''
Remember! Command line args are in sys.argv[1], sys.argv[2] ... sys.argv[0] is the script name itself and can be ignored This'll be needed if we get far enough along to allow calling the program on paths from the command line instead of hard-coding pieces.
'''

def genMat(transProbs):
    matInd = 0
    for prob in sorted(transProbs.values()):
        if matInd == 8:
            break
        print prob
        matInd = matInd + 1

def attraction(piece):
    matrix1 = [  [3,5,6,2],[4,5,2,3]  ]
    matrix2 = [  [7,4,2,6],[3,5,6,7]  ]
    mse=0
    row=0
    while row<2:
        print row
        col=0
        print 
        while col<4:
            difference = matrix1 [row][col] - matrix2 [row][col]
            print difference
            math.fabs(difference)
            mse = mse + (difference * difference)
        col=col+1
        row=row+1
        #print mse


# Run
n = 0
for piece in pieceList:
    pitchList = pitchList(piece)
    noteFreqs = noteFreqs(pitchList)
    totalNotes = totalNotes(noteFreqs)
    transFreqs = transFreqs(pitchList, totalNotes)
    indProbs = indProbs(noteFreqs)
    totalTrans = totalTrans(transFreqs)
    transProbs = transProbs(transFreqs, totalNotes)

 # Header for piece-processing
    print '-'*64
    print piece
    print '-'*64
    print '\n'

    genMat(transProbs)

    #print sorted(transProbs.values())

    #for prob in transProbs:
    #    print transProbs[prob]

    # Process the next piece!
    n = n + 1
