#!/usr/bin/env python

# Required modules installed in Python
import sys
import os

# Modules in this directory
import corporaIO 
# import chainBuilder
# import coprViz

# Pieces to be processed
pieceList = ['supplementary corpora/myboy.mid','supplementary corpora/WTK1.mid']

def main():
    n = 0
    for piece in pieceList:
        added = corporaIO.addPiece(piece)
        print pieceList[n]
        print added
        n = n + 1

    # Remember! Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Call the main() function and run the program
if __name__ == '__main__':
    main()
