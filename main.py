#!/usr/bin/env python

# Required modules installed in Python
import sys
import os

# Modules in this directory
import corporaIO 
import chainBuilder

def main():
    stream1 = corporaIO.addFile('supplementary corpora/myboy.mid')
    stream2 = corporaIO.addFile('supplementary corpora/WTK1.mid')
    print len(stream1)
    print len(stream2)

    # Remember! Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Call the main() function and run the program
if __name__ == '__main__':
    main()
