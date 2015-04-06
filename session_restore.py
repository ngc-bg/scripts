#!/usr/bin/python

import json, sys

def write(n, content):
    fout = open('sessionstore.%d' % (n,), 'wb')
    try:
        fout.write(unicode(content).encode('utf-8'))
    finally:
        fout.close()

if len(sys.argv) < 2:
    print >>sys.stderr, ("Usage: sesion_restore.py sessionstorefile\n"
                         "Extracted sessions will be placed in sessionstore.0,1,etc.\n")
    sys.exit(1)

fin = open(sys.argv[1], 'rb')
try:
    n = 0
    json = json.load(fin)

    for window in json["windows"]:
        for tab in window["tabs"]:
            entries = tab["entries"]
            if len(entries) > 0 and entries[0]["url"] == "about:sessionrestore":
                innerjson = entries[0]["formdata"]["#sessionData"]
                write(n, innerjson)
                n += 1

        for closedtab in window["_closedTabs"]:
            entries = closedtab["state"]["entries"]
            if len(entries) > 0 and entries[0]["url"] == "about:sessionrestore":
                innerjson = entries[0]["formdata"]["#sessionData"]
                write(n, innerjson)
                n += 1
finally:
    fin.close()