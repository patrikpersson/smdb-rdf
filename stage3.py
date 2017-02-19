#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import os.path
import sys
import urllib2
from xml.dom import minidom

# ----------------------------------------------------------------------------
# Steg 3
#
# Går igenom samtliga RDF-filer för programmen och skriver ut dem som CSV,
# redo att importeras i Excel eller Google Docs.
#
# Kör som (om du vill ha CSV för 1981 års program)
#
#   python stage3.py rdf-1981/ > 1981.csv
#
# Detta förutsätter att stage2.py har körts och resultatet finns i
# katalogen rdf-1981.
# ----------------------------------------------------------------------------

if len(sys.argv) < 2:
    print "användning:"
    print "python %s <rdf-katalog>" % os.path.basename(sys.argv[0])
    sys.exit(-1)

basedir = sys.argv[1]

# UTF-8 marker
sys.stdout.write("%c%c%c" % (0xEF, 0xBB, 0xBF))

def collect_text(node):
    text_data = []
    for node in node.childNodes:
        if node.nodeType == node.TEXT_NODE:
            text_data.append(node.data.strip().strip('.').replace('\n', ' '))
    return ' '.join(text_data)

for _, dirs, _ in os.walk(basedir):
    for dir in dirs:
        for f in os.listdir(basedir + '/' + dir):
            rdf = '%s/%s/%s' % (basedir, dir, f)
            xml = minidom.parse(rdf)
            date = collect_text(xml.getElementsByTagName('dc:date')[0])
            title = collect_text(xml.getElementsByTagName('dc:title')[0])
            channel = collect_text(xml.getElementsByTagName('po:channel')[0])
            descr = collect_text(xml.getElementsByTagName('dc:description')[0])
            
            print ("%s;%s;%s;%s" % (date, channel, title, descr)).encode('utf-8')
