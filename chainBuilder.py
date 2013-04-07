'''
Bayes' Theorem:
    P(x|y) = P(x)P(y|x)/P(y)
'''

# P of each note in each piece given the immediately preceding note.
def probNext()

def noteProb(noteFreqs):
    # Dictionary of overall note probabilities per piece.
    total = float(len(noteFreqs))
    noteProbs = {}
    for notes, freqs in noteFreqs.items():
        noteProbs[notes] = freqs / total
    return noteProbs

# This needs to return a 12x12 matrix of note frequencies; a transition table for the particular piece.
# return something interpretable by chainBuilder.py?
