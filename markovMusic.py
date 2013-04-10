#!/usr/bin/env python

# Required modules installed in Python
import sys
import os
import math
import re

# Modules in this directory
from corporaIO import getPitchList
from chainBuilder import *
import corpViz

# Pieces to be processed; relative to . or corpus
# Change to read from file with one filename per line
pieceList = ['supplementary corpora/BachCelloSuiteP1.mid', 'supplementary corpora/BachCelloSuiteP5.mid', 'supplementary corpora/Battle_Hymn_Of_The_Republic_5.mid', 'supplementary corpora/ShuleaAgra.mid', 'supplementary corpora/WTK1.mid', 'supplementary corpora/WTK6.mid', 'supplementary corpora/amazinggrace.mid', 'supplementary corpora/americathebeautiful.mid', 'supplementary corpora/anorthco.mid', 'supplementary corpora/dabblinginthedew.mid', 'supplementary corpora/myboy.mid', 'supplementary corpora/thenoblemanswedding.mid']


noteNames = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

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
    probMat = [[[0]for i in xrange(12)] for j in xrange(12)]
    # Make column 1; base values.
    for note, prob in noteProbs.items():
        i = 0
        while i < 12:
            if noteNames[i] == note:
                probMat[i][0] = prob
            i = i + 1
    # Populate matrix with transition probabilities
    for trans, prob in transProbs.items():
        i = 0
        while i < 12:
            j = 0
            try:
                match = re.search(r'^.\#', trans).group()
                if noteNames[i] == match:
                    probMat[i][j] = prob
            except: 
                match = re.search(r'^.', trans).group() 
                if noteNames[i] == match:
                    probMat[i][j] = prob
            while j < 12:
                try:
                    match = re.search(r'.\#$', trans).group()
                    if noteNames[i] == match:
                        probMat[i][j] = prob
                except: 
                    match = re.search(r'.$', trans).group() 
                    if noteNames[i] == match:
                        probMat[i][j] = prob
                j = j + 1
            i = i + 1
    return probMat

# Accepts two probability matrices and returns a 'difference matrix'.
def meanSquareError(probMat1, probMat2):
    meanSquareError = 0
    i = 0
    while i < 2:
        print i
        j = 0
        print j
        while j < 4:
            totDiff = probMat1[i][j] - probMat2[i][j]
            print totDiff
            math.fabs(totDiff)
            meanSquareError = meanSquareError + (totDiff * totDiff)
            j = j + 1
        i = i + 1
        print meanSquareError

# Run
pieceNum = 0
for piece in pieceList:
# Header for printed output 
    print '\n'
    print '-'*64
    pieceID = re.sub(r'(.+)\/(.+)',r'\2', piece)
    print pieceID
    print '-'*64
    print '\n'
# Transition matrix for piece.
    probMat1 = getProbMat(piece)
    print probMat1
    nextPieceNum = pieceNum + 1
    for next in pieceList[nextPieceNum:]:
        print '\n'
        print '-'*64
        nextID = re.sub(r'(.+)\/(.+)',r'\2', next)
        print pieceID + ' to ' + nextID
        print '-'*64
        print '\n'
        probMat2 = getProbMat(piece)
        meanSquareError(probMat1, probMat2)

        print 'MATRIX?'
        nextPieceNum = nextPieceNum + 1
    pieceNum = pieceNum + 1

    #for prob in transProbs:
    #    print transProbs[prob]

    # Process the next piece!
try: 
    if sys.argv[1] == 'graph':
        print 'GRAPH CALLED'
        #corpViz
    elif sys.argv[1] == 'print':
        print 'PRINT CALLED'
except:
    sys.exit(0)
