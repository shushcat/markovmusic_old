from music21 import *
from music21 import corpus

'Returns a list of pitches when called on either a path to a valid file type or the name of a piece in the music21 corpus.'

# Makes music21.stream.Score objects and converts them to lists of pitches.
def pitchList(piece):
    # Parses and flattens so notes can be linearly compared. Flattening precedence is: offset time, pitch (low to high?), classSortOrder (notes, accidentals, rests, etc. Not important here since we're just extracting all the notes anyway.
    try:
        added = converter.parseFile(piece)
    except:
        added = corpus.parse(piece)
    piecePitches = [str(p) for p in added.pitches]
    return piecePitches
