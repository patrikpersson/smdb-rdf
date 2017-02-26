#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ============================================================================
# smdb-rdf:
# Samlar ihop RDF-filer (XML) från smdb.kb.se och skapar en .csv-fil.
# (c) Patrik Persson 2017. Se README.md för instruktioner, LICENSE för licens.
# ============================================================================

import os
import os.path
import sys
import urllib2
from xml.dom import minidom

# ----------------------------------------------------------------------------

def collect_text(node):
    text_data = []
    for node in node.childNodes:
        if node.nodeType == node.TEXT_NODE:
            text_data.append(node.data.strip().strip('.').replace('\n', ' ').replace(';',''))
    return ' '.join(text_data)

# ----------------------------------------------------------------------------

if len(sys.argv) != 2:
    print "användning:"
    print "python %s <rdf-katalog>" % os.path.basename(sys.argv[0])
    sys.exit(-1)

basedir = sys.argv[1]

# UTF-8 marker
sys.stdout.write("%c%c%c" % (0xEF, 0xBB, 0xBF))

for _, dirs, _ in os.walk(basedir):
    for dir in dirs:
        for f in os.listdir(basedir + '/' + dir):
            rdf = '%s/%s/%s' % (basedir, dir, f)
            xml = minidom.parse(rdf)
            date = collect_text(xml.getElementsByTagName('dc:date')[0])
            title = collect_text(xml.getElementsByTagName('dc:title')[0])
            channel = collect_text(xml.getElementsByTagName('po:channel')[0])
            descr = collect_text(xml.getElementsByTagName('dc:description')[0])
            
            print ("%s;%s;%s;%s" % (date, channel, title, descr)).replace('"', '').replace("'","").encode('utf-8');
