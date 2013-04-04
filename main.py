#!/usr/bin/env python

# Required modules installed in Python
import sys
import os

# Modules in this directory
import corporaIO 


'''
The main methods and maybe some other stuff.

Preliminary notes:
    Bayes' Theorem:
    P(x|y) = P(x)P(y|x)/P(y)
'''

def main():
    print 'Hello there,', sys.argv[1],'.'
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
    corporaIO.thatone()
