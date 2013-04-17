#!/usr/bin/env python
'Weighted graph of precessed corpora via GraphViz.'
from subprocess import Popen, PIPE
import subprocess
import sys
import re

HEADER = "digraph  dependencies { layout=neato;   splines=true; overlap=scalexy;  rankdir=LR; weight=2;"
FOOTER = "}"

color = 'grey'
penWidth = 1
style = 'filled'

piecesAndLinks = []
mSEs = []
graphOut = [HEADER]

def call_dot(instr):
    'call dot, returning stdout and stdout'
    dot = Popen('dot -Tgv'.split(), stdout=PIPE, stderr=PIPE, stdin=PIPE)
    return dot.communicate(instr)

# Run
if __name__ == '__main__':
    # Parse data into lists
    input = open('out.txt', 'rU')
    for line in input:
        if re.search(r'(.+.mid) to (.+.mid)', line):
            parsed = re.sub(r'(.+)(.mid) to (.+)(.mid)', r'\1 -> \3', line).rstrip()
            piecesAndLinks.append(parsed)
        elif re.search(r'(MSE: )(.+)', line):
            if re.search(r'.+e.+', line):
                parsed = 1
            else:
                parsed = (float(re.sub(r'(MSE: )(.+)', r'\2', line).rstrip()))
            mSEs.append(parsed)
            print mSEs

    for trans in piecesAndLinks:
        # linking proportional to MSE?
#        graphOut.append(trans + ('[dir=none][shape=box][penwidth=%d][fillcolor=%s][style=%s][weight=%d]' % (penWidth, color, 'invis', mSEs[piecesAndLinks.index(trans)])))
        graphOut.append(trans + ('[dir=none][shape=box][penwidth=%d][fillcolor=%s][len=%g]' % (penWidth, color, mSEs[piecesAndLinks.index(trans)])))

    # potentially append genre information
#    print ('Making and Linking Tag Nodes')
#    for datum in data:
#        for tag in datum.get('tags',''):
#                lines.append('"%s" -> "%s";' % (datum['uuid'], tag))
#                lines.append('"%s"[shape=square][fontsize=24.0][penwidth=8]' % (tag))
#                continue

    graphOut.append(FOOTER)

    gv, err = call_dot('\n'.join(graphOut))
    if err != '':
        print ('Error calling dot:')
        print (err.strip())

    print ('Writing to /tmp/corpViz.gv')
    with open('/tmp/corpViz.gv', 'w') as f:
        f.write(gv)

subprocess.call("open /tmp/corpViz.gv", shell = True)
