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
# python stage1.py rdf-1981/001697731.rdf
#
# eller
#
# python stage1.py rdf-1981/*.rdf
#
# De refererade RDF-filerna lagras i kataloger, exempelvis i
# exemplet ovan
#
# rdf-1981/001697731/1.rdf
# ----------------------------------------------------------------------------

if len(sys.argv) < 2:
    print "användning:"
    print "python %s <rdf-fil> [rdf-fil...]" % sys.argv[0]
    sys.exit(-1)

# ----------------------------------------------------------------------------

for rdf in sys.argv[1:]:
    print os.path.basename(rdf)

    subdir = os.path.dirname(rdf) + '/' + os.path.basename(rdf).strip('.rdf')
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    for part in minidom.parse(rdf).getElementsByTagName('dcterms:hasPart'):
        url = part.attributes['rdf:resource'].value
        print "  %s" % os.path.basename(url)
        filename = subdir + '/' + os.path.basename(url) + '.rdf'
        xml = urllib2.urlopen(url + '.rdf').read()
        file = open(filename, 'w')
        file.write(xml)
        file.close()
