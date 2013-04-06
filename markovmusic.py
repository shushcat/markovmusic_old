#!/usr/bin/env python

# Required modules installed in Python
import sys
import os

# Modules in this directory
import corporaIO 
# import chainBuilder
# import coprViz

def main():
    fileList = ['supplementary corpora/myboy.mid','supplementary corpora/WTK1.mid']
    for file in fileList:
        added = corporaIO.addPiece(file)
        print added

    # Remember! Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Call the main() function and run the program
if __name__ == '__main__':
    main()
