from music21 import *
from music21 import corpus

'Returns a list of pitches when called on a path to a valid file type.'

# Makes music21.stream.Score objects
def listPitches(piece):
    # Parses and flattens so notes can be linearly compared. Flattening precedence is: offset time, priority (low to high?), classSortOrder and takes place automatically when applying the str() method.
    added = converter.parseFile(piece)
    piecePitches = [str(p) for p in added.pitches]
    return piecePitches
