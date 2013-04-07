#!/usr/bin/env python
'Weighted graph of processed corpora via GraphViz.'
from subprocess import Popen, PIPE
import subprocess
import sys
import textwrap

# Wrap node label text at this number of characters
charsPerLine = 20;

# Color defs; figure these out later.
# full list of colors here: http://www.graphviz.org/doc/info/colors.html
aColor = 'red2'
anotherColor = 'green';

#The width of the border around the nodes:
penWidth = 1

# Arrow heads will need attention...
arrowHead = 'dot'

#Spread nodes on page
HEADER = "digraph  dependencies { layout=neato;   splines=true; overlap=scalexy;  rankdir=LR; weight=2;"

#More information on setting up graphviz: http://www.graphviz.org/doc/info/attrs.html

FOOTER = "}"

validUuids = list()

def call_dot(instr):
    'call dot, returning stdout and stdout'
    dot = Popen('dot -Tgv'.split(), stdout=PIPE, stderr=PIPE, stdin=PIPE)
    return dot.communicate(instr)

def corpora(pieces):

    #print data
    maxAttraction= -9999;
    for datum in data:
        if float(datum['attraction']) > maxAttraction:
            maxAttraction = float(datum['attraction'])

    # first pass: labels
    lines = [HEADER]
    print ('Printing Labels')
    for datum in data:
        validUuids.append(datum['uuid'])
        if datum['description']:

            style = ''
            color = ''
            style = 'filled'

            if datum['status']=='pending':
                prefix = datum['id']
                if not datum.get('depends','') : color = unblockedColor
                else :
                    hasPendingDeps = 0
                    for depend in datum['depends'].split(','):
                        for datum2 in data:
                            if datum2['uuid'] == depend and datum2['status'] == 'pending':
                               hasPendingDeps = 1
                    if hasPendingDeps == 1 : color = blockedColor
                    else : color = unblockedColor

            elif datum['status'] == 'waiting':
                prefix = 'WAIT'
                color = waitColor
            elif datum['status'] == 'completed':
                prefix = 'DONE'
                color = doneColor
            elif datum['status'] == 'deleted':
                prefix = 'DELETED'
                color = deletedColor
            else:
                prefix = ''
                color = 'white'


            if float(datum['urgency']) == maxUrgency:
                color = maxUrgencyColor

            label = '';
            descriptionLines = textwrap.wrap(datum['description'],charsPerLine);
            for descLine in descriptionLines:
                label += descLine+"\\n";
    
            lines.append('"%s"[shape=box][penwidth=%d][label="%s\:%s"][fillcolor=%s][style=%s]' % (datum['uuid'], penWidth, prefix, label, color, style))
            #documentation http://www.graphviz.org/doc/info/attrs.html


# Examples of modification to be applied to specific classes of nodes
    # second pass: dependencies
    print ('Resolving Dependencies')
    for datum in data:
        if datum['description']:
            for dep in datum.get('depends', '').split(','):
                #print ("\naaa %s" %dep)
                if dep!='' and dep in validUuids:
                    lines.append('"%s" -> "%s"[dir=%s];' % (dep, datum['uuid'], dir))
                    continue

    # third pass: projects
    print ('Making and Linking Project Nodes')
    for datum in data:
        for proj in datum.get('project', '').split(','):
            if proj != '':
                lines.append('"%s" -> "%s"[dir=both][arrowtail=odot];' % (proj, datum['uuid']))
                lines.append('"%s"[shape=circle][fontsize=40.0][penwidth=16][color=gray52]' % (proj))
                continue

    # third pass: tags
    print ('Making and Linking Tag Nodes')
    for datum in data:
        for tag in datum.get('tags',''):
            if tag != '':
                lines.append('"%s" -> "%s";' % (datum['uuid'], tag))
                lines.append('"%s"[shape=square][fontsize=24.0][penwidth=8]' % (tag))
                continue

    lines.append(FOOTER)

    print ('Calling dot')
    gv, err = call_dot('\n'.join(lines))
    if err != '':
        print ('Error calling dot:')
        print (err.strip())

    print ('Writing to corpViz.gv')
    with open('/tmp/corpViz.gv', 'w') as f:
        f.write(gv)

subprocess.call("open /tmp/corpViz.gv", shell = True)
