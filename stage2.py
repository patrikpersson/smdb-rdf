#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os.path
import sys
import urllib2
from xml.dom import minidom

# ----------------------------------------------------------------------------
# Steg 2
#
# Går igenom en RDF-fil och laddar ner alla refererade
# RDF-filer (för individuella program).
#
# Kör som (om du vill ha RDF-filerna för 1981 års TV-program)
#
#   python stage1.py rdf-1981/001697731.rdf
#
# eller
#
#   python stage1.py rdf-1981/*.rdf
#
# De refererade RDF-filerna lagras i kataloger, exempelvis för
# exemplet ovan
#
# rdf-1981/001697731/1.rdf
# rdf-1981/001697731/2.rdf
# rdf-1981/001697731/3.rdf
# ...
#
# Detta förutsätter att stage1.py har körts för 1981
# ----------------------------------------------------------------------------

if len(sys.argv) < 2:
    print "användning:"
    print "python %s <rdf-fil> [rdf-fil...]" % os.path.basename(sys.argv[0])
    sys.exit(-1)

# ----------------------------------------------------------------------------

for rdf in sys.argv[1:]:
    print os.path.basename(rdf)

    subdir = os.path.dirname(rdf) + '/' + os.path.basename(rdf).strip('.rdf')
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    for part in minidom.parse(rdf).getElementsByTagName('dcterms:hasPart'):
        partname = os.path.basename(part.attributes['rdf:resource'].value)
        dir = os.path.basename(rdf).strip('.rdf')
        url = 'https://smdb.kb.se/catalog/id/' + dir + '/' + partname + '.rdf'
        print "  %s" % partname
        #print "url=" + url
        filename = subdir + '/' + os.path.basename(url)
        #print "  %s" % filename
        xml = urllib2.urlopen(url + '.rdf').read()
        file = open(filename, 'w')
        file.write(xml)
        file.close()