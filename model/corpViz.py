#!/usr/bin/env python
"""
Weighted graph of precessed corpora via GraphViz.

Can be called on a text file containing output, or can accept piped input, from markovMusic.py.
"""
from subprocess import Popen, PIPE
import subprocess
import sys
import platform
import re

HEADER = "digraph { "
FOOTER = "}"

color = 'grey'
penWidth = 1
style = 'filled'
mSEs = []
graphOut = [HEADER]

# Parse data into lists
piecesAndLinks = []
def getPiecesAndLinks(flag):
    if flag == '-':
        input = sys.stdin.readlines()
    else:
        input = open(flag, 'rU')
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
    return piecesAndLinks

def call_dot(instr):
    'call dot, returning stdout and stdout'
    dot = Popen('dot -Tgv'.split(), stdout=PIPE, stderr=PIPE, stdin=PIPE)
    return dot.communicate(instr)

# Run
if __name__ == '__main__':
    try:
        flag = sys.argv[1]
    except:
        sys.exit("No data provided to corpViz.")
    piecesAndLinks = getPiecesAndLinks(flag)
    for trans in piecesAndLinks:
        # Weight links proportionally to MSE
        weight = 1000 - (mSEs[piecesAndLinks.index(trans)] * 100000)
        print weight
        graphOut.append(trans + ('[dir=none][shape=box][penwidth=%d][fillcolor=%s][weight=%d]' % (penWidth, color, weight)))

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

    print ('Writing to corpViz-out.gv')
    with open('corpViz-out.gv', 'w') as f:
        f.write(gv)

    if platform.system() == 'Darwin':
        try:
            subprocess.call("open /tmp/corpViz.gv", shell = True)
        except:
            print "Can't find GraphViz...."
