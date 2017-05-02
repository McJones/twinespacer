import codecs
import sys
import re
from bs4 import BeautifulSoup
from graphviz import Digraph

if len(sys.argv) < 3:
    print("insufficient arguments, format is: twinespacer.py inputFile outputFile")
    print("you can optionally supply a graph style that matches graphviz engines")
    sys.exit()

inputFile = sys.argv[1]
outputFile = sys.argv[2]

if len(sys.argv) == 4:
    engine = sys.argv[3]
else:
    engine = "dot"

spacing = 125

data = open(inputFile).read()
soup = BeautifulSoup(data,'html.parser')
nodes = dict()

# grabbing all the twine nodes from the story
for node in soup.find_all('tw-passagedata'):
    pid = int(node.get('pid'))
    name = node.get('name')
    body = re.findall("\[\[.+?\]\]",node.string,re.DOTALL)
    nodes[pid] = {"name":name,"body":body}

# hahaha efficiency is for suckers!
for key, node in nodes.iteritems():
    connections = list()
    for link in node["body"]:
        for nodeKey, iNode in nodes.iteritems():
            if iNode["name"] in link:
                connections.append(nodeKey)
    if len(connections) > 0:
        nodes[key]["links"] = connections

# creating the graph
dot = Digraph(name='Twine Story')
dot.engine = engine
dot.format = "plain"
for key, node in nodes.iteritems():
    dot.node(str(key), node["name"])
    if "links" in node:
        for link in node["links"]:
            dot.edge(str(key),str(link))
# exporting the whole thing to twine.dot.plain
dot.render('twine.dot')

# modifying the twine file to have the new positions
with open('twine.dot.plain') as file:
    for line in file:
        chunks = line.split()
        if chunks[0] == "node":
            pid = chunks[1]
            x = str(float(chunks[2]) * spacing)
            y = str(float(chunks[3]) * spacing)
            node = soup.find(pid=pid)
            node['position'] = str(x) + "," + str(y)
            print("moving node " + pid + " to " + x + "," + y)

# exporting the whole thing
html = soup.prettify()
file = codecs.open(outputFile, 'w', encoding='utf8')
file.write(html)
file.close()