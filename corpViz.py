#!/usr/bin/env python
# Potentially extraneous.
from subprocess import Popen, PIPE
import subprocess
import textwrap
# Visualization libraries for access and manipulation of dot files. These are vital.
import sys
sys.path.append('..')
# sys.path.append('/usr/lib/graphviz/pythn/')
# sys.path.append('/usr/lib64/graphviz/python/')

# Wrap label text at this number of characters
# charsPerLine = 20;


# Full list of colors here: http://www.graphviz.org/doc/info/colors.html
# blockedColor = 'gold4'
# maxUrgencyColor = 'red2' # Color of the tasks that have absolutely the highest urgency
# unblockedColor = 'green'
# doneColor = 'grey'
# waitColor = 'white'
# deletedColor = 'pink';

# Import graphviz
import sys
import pydot

# Import from pydot
from pydot.object import graph
from pydot.classes.digraph import digraph
from pydot.algorithms.searching import breadth_first_search
from pydot.readwrite.dot import write

# Graph creation
gr = graph()

# Add nodes and edges
gr.add_nodes(["Portugal","Spain","France","Germany","Belgium","Netherlands","Italy"])
gr.add_nodes(["Switzerland","Austria","Denmark","Poland","Czech Republic","Slovakia","Hungary"])
gr.add_nodes(["England","Ireland","Scotland","Wales"])

gr.add_edge(("Portugal", "Spain"))
gr.add_edge(("Spain","France"))
gr.add_edge(("France","Belgium"))
gr.add_edge(("France","Germany"))
gr.add_edge(("France","Italy"))
gr.add_edge(("Belgium","Netherlands"))
gr.add_edge(("Germany","Belgium"))
gr.add_edge(("Germany","Netherlands"))
gr.add_edge(("England","Wales"))
gr.add_edge(("England","Scotland"))
gr.add_edge(("Scotland","Wales"))
gr.add_edge(("Switzerland","Austria"))
gr.add_edge(("Switzerland","Germany"))
gr.add_edge(("Switzerland","France"))
gr.add_edge(("Switzerland","Italy"))
gr.add_edge(("Austria","Germany"))
gr.add_edge(("Austria","Italy"))
gr.add_edge(("Austria","Czech Republic"))
gr.add_edge(("Austria","Slovakia"))
gr.add_edge(("Austria","Hungary"))
gr.add_edge(("Denmark","Germany"))
gr.add_edge(("Poland","Czech Republic"))
gr.add_edge(("Poland","Slovakia"))
gr.add_edge(("Poland","Germany"))
gr.add_edge(("Czech Republic","Slovakia"))
gr.add_edge(("Czech Republic","Germany"))
gr.add_edge(("Slovakia","Hungary"))

# Draw as PNG
dot = write(gr)
gvv = gv.readstring(dot)
gv.layout(gvv,'dot')
gv.render(gvv,'png','europe.png')
