from music21 import corpus

catalog = stream.Score()
for work in corpus.beethovenStringQuartets():
    if work.flat.getElementsByClass(meter.TimeSignature)[0].ratioString == '6/8':
        catalog.append(work.measureRange(0,2))
catalog.show() 
