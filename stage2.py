#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ============================================================================
# smdb-rdf:
# Samlar ihop RDF-filer (XML) från smdb.kb.se och skapar en .csv-fil.
# (c) Patrik Persson 2017. Se README.md för instruktioner; LICENSE för licens.
# ============================================================================

import os.path
import sys
import urllib2
from xml.dom import minidom

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
