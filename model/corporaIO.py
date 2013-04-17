from music21 import *
from music21 import corpus
import re

'Returns a list of pitches when called on either a path to a valid file type or the name of a piece in the music21 corpus.'

# Makes music21.stream.Score objects and converts them to lists of notes.
def getPitchList(piece):
    # Parses and flattens so notes can be linearly compared. Flattening precedence is: offset time, pitch (low to high?), classSortOrder (notes, accidentals, rests, etc., but not important here since we're just extracting all the notes anyway)
    try:
        added = converter.parseFile(piece)
    except:
        added = corpus.parse(piece)
    unformattedList = [str(p) for p in added.pitches]
    formattedList = []
    for pitch in unformattedList:
        if re.search(r'.+-\d', pitch):
            pitch = re.sub(r'(.+)-(\d)', r'\1\2', pitch)
        formattedList.append(pitch)
    return formattedList
