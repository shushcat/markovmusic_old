#!/usr/bin/env python

# Required modules installed in Python
import sys
import os

# Modules in this directory
import corporaIO 
import chainBuilder
# import corpViz

# Pieces to be processed
pieceList = ['supplementary corpora/myboy.mid','supplementary corpora/WTK1.mid']
'''
Remember! Command line args are in sys.argv[1], sys.argv[2] ... sys.argv[0] is the script name itself and can be ignored This'll be needed it we get far enough along to allow calling the program on paths from the command line instead of hard-coding pieces.
'''

def main():
    n = 0
    for piece in pieceList:
        added = corporaIO.addPiece(piece)
        print pieceList[n]
        print added
        print chainBuilder.getFreqs(added)
        n = n + 1


# Call the main() function and run the program
if __name__ == '__main__':
    main()
