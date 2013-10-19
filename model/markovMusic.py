#!/usr/bin/env python

"""
Call on a file containing paths to pieces, one piece per line. Lines which either begin with a # or are blank are ignored.
"""

# Required modules installed in Python
import sys
import os
import math
import re

# Modules in this directory
from corporaIO import getPitchList
from chainBuilder import *

# Setting up pieces for processing
pieceList = []
def getPieceList(fileName):
    input = open(fileName, 'rU')
    for line in input:
        if not re.search(r'^#', line) and line.rstrip() != '':
            pieceList.append(line.rstrip())
    return pieceList

# Note dictionary
noteNames = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
# Add list or dictionary mapping possible transitions to intervals.

# Builds a transition probability matrix for a given piece
def getProbMat(piece):
    thisPiece = piece
    pitchList = getPitchList(thisPiece)
    noteFreqs = getNoteFreqs(pitchList)
    totalNotes = getTotalNotes(noteFreqs)
    transFreqs = getTransFreqs(pitchList, totalNotes)
    noteProbs = getNoteProbs(noteFreqs)
    totalTrans = getTotalTrans(transFreqs)
    transProbs = getTransProbs(transFreqs, totalNotes)
#    probMat = getProbMat(noteProbs, transProbs)
    # Make matrix; populate with 0s
    probMat = [[0 for i in xrange(12)] for j in xrange(12)]
    # Populate matrix with probabilities
    i = 0
    while i < 12:
        j = 0
        while j < 12:
       	    a = noteNames[i]
       	    b = noteNames[j]
       	    try:
       	        c = transProbs[a + b]
       	        probMat[i][j] = c
       	    except:
       	        probMat[i][j] = 0
            j = j + 1
        i = i + 1
    return probMat

# Accepts two probability matrices and returns their mean square error.
def meanSquareError(probMat1, probMat2):
    meanSquareError = 0
    i = 0
    while i < 12:
        j = 0
        totDiff = 0
        while j < 12:
            addrIn1 = probMat1[i][j]
            addrIn2 = probMat2[i][j]
            totDiff =  math.fabs(addrIn1 - addrIn2)
            meanSquareError = meanSquareError + (totDiff * totDiff)
            j = j + 1
        i = i + 1
        return meanSquareError

# Run
if __name__ == '__main__':
    # Load pieces from pieceList.txt
    pieceList = getPieceList(sys.argv[1])
    print pieceList
    for piece in pieceList:
        pieceNum = pieceList.index(piece)
        probMat1 = getProbMat(piece)
        # Header
        print '\n'
        print '-'*64
        pieceID = re.sub(r'(.+)\/(.+)',r'\2', piece)
        print pieceID
        print '-'*64
        print '\n'
        # Base probMat
        print probMat1
        nextPieceNum = pieceNum + 1
        for next in pieceList[nextPieceNum:]:
            # Sub-header
            print '\n'
            print '-'*64
            nextID = re.sub(r'(.+)\/(.+)',r'\2', next)
            print pieceID + ' to ' + nextID
            print '-'*64
            print '\n'
            # Comparison probMat
            probMat2 = getProbMat(next)
            # Mean square error
            print 'MSE: ' + str(meanSquareError(probMat1, probMat2))
