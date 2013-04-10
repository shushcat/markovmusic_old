#!/usr/bin/env python

# Required modules installed in Python
import sys
import os
import math

# Modules in this directory
from corporaIO import pitchList 
from chainBuilder import *
import corpViz

# Pieces to be processed; relative to . or corpus
pieceList = ['supplementary corpora/WTK1.mid']

'''
Remember! Command line args are in sys.argv[1], sys.argv[2] ... sys.argv[0] is the script name itself and can be ignored This'll be needed if we get far enough along to allow calling the program on paths from the command line instead of hard-coding pieces.

Also need this knowledge for selectively calling corpViz methods.
'''

def genMat(noteProbs, transProbs):
    # Make column 1.
    # Sort by prob, high to low (but return keys too!). This is truncating the list to 8
# For matrices [A, A# B, C, C#, D, D#, E, F, F#, G, G#] -> [1,2,3,4,5,6,7,8,9,10,11,12]
    index = 0
    probMat = [[] for i in xrange(12)]
    print noteProbs
    sortedNotes = sorted(noteProbs.keys())
    print sortedNotes
    # Send noteProbs to index 1 of each matrix
    # Need to map addresses by pitch.
    # ij to populate matrix
    for item in sortedNotes:
        if index == 12:
            break
        probMat[index].append(item)
        index = index + 1
    return probMat

# Accepts two probability matrices and returns a difference matrix.
def meanSquareError(probMat1, probMat2):
    probMat1 = [[3,5,6,2], [4,5,2,3]]
    probMat2 = [ [7,4,2,6], [3,5,6,7] ]
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
        print mse

# Run
n = 0
for piece in pieceList:
    pitchList = pitchList(piece)
    noteFreqs = noteFreqs(pitchList)
    totalNotes = totalNotes(noteFreqs)
    transFreqs = transFreqs(pitchList, totalNotes)
    noteProbs = noteProbs(noteFreqs)
    totalTrans = totalTrans(transFreqs)
    transProbs = transProbs(transFreqs, totalNotes)
    genMat = genMat(noteProbs, transProbs)

 # Header for piece-processing
    print '-'*64
    print piece
    print '-'*64
    print '\n'
    print noteProbs

    genMat
    print 'Transition matrix.'
    print genMat
    

#    print 'Transition probabilities:'
#    print transProbs

    #print sorted(transProbs.values())

    #for prob in transProbs:
    #    print transProbs[prob]

    # Process the next piece!
    n = n + 1
try: 
    sys.argv[1] == 'graph'
    print 'GRAPH CALLED'
except:
    sys.exit(0)

    #corpViz
