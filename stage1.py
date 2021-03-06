#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ============================================================================
# smdb-rdf:
# Samlar ihop RDF-filer (XML) från smdb.kb.se och skapar en .csv-fil.
# (c) Patrik Persson 2017. Se README.md för instruktioner, LICENSE för licens.
# ============================================================================

import HTMLParser
import os
import os.path
import sys
import urllib2

# ----------------------------------------------------------------------------

if len(sys.argv) < 2:
    print "användning:"
    print "python %s [-radio] <årtal>" % os.path.basename(sys.argv[0])
    sys.exit(-1)

if sys.argv[1] == "-radio":
    YEAR = sys.argv[2]
    TYPE = "radio"
else:
    YEAR = sys.argv[1]
    TYPE = "tv"

DIRECTORY = 'rdf-%s-%s' % (TYPE, YEAR)

if not os.path.exists(DIRECTORY):
    os.makedirs(DIRECTORY)

# ----------------------------------------------------------------------------

class TVTableParser(HTMLParser.HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            wanted = False
            url = None
            for (name, value) in attrs:
                if name == 'class' and value == 'recordLink':
                    wanted = True
                elif name == 'href':
                    url = value
            if wanted:
                name = os.path.basename(url)
                print "  %s" % name
                xml = urllib2.urlopen('https://smdb.kb.se' + url + '.rdf').read()
                f = open(DIRECTORY + '/' + name + '.rdf', 'w')
                f.write(xml)
                f.close()

# ----------------------------------------------------------------------------

month_lengths = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

for month in range(1, 13):
    for day in range(1, month_lengths[month - 1] + 1):
        day_str = "%s%02d%02d" % (YEAR, month, day)
        print day_str
        url = 'https://smdb.kb.se/catalog/search?q=typ%3A' + TYPE + '+datum%3A' + day_str + '&x=0&y=0'

        html = urllib2.urlopen(url).read()
        TVTableParser().feed(html)
