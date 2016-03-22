#!/usr/bin/env python3
#-*-coding:utf-8-*-
# Usage: ./plantuml2mysql <dbsource.plu> <dbname>
# Author: Alexander I.Grafov <grafov@gmail.com>
# The code is public domain.

CHARSET="utf8_unicode_ci"

import sys

tmap = {}
cmap = {}

def tmeta():
    meta = False
    with open(sys.argv[1]) as src:
        data = src.readlines()
    for l in data:
        l = l.strip()
        if not l:
            continue
        if l == "@starttmeta":
            meta = True
            continue
        if not meta:
            continue
        if l == "--":
            continue
        if l == "@endtmeta":
            meta = False
            break
        if meta:
            i = l.split("|")
            lname = i[0]
            ldef = i[1]
            tmap.update({ lname : ldef })
            continue

def cmeta():
    meta = False
    with open(sys.argv[1]) as src:
        data = src.readlines()
    for l in data:
        l = l.strip()
        if not l:
            continue
        if l == "@startcmeta":
            meta = True
            continue
        if not meta:
            continue
        if l == "--":
            continue
        if l == "@endcmeta":
            meta = False
            break
        if meta:
            i = l.split("|")
            lname = i[0]
            ldef = i[1]
            cmap.update({ lname : ldef })
            continue

def main():
    tmeta()
    cmeta()
    uml = False; table = False; field = False; pk = False
    primary = []
    with open(sys.argv[1]) as src:
        data = src.readlines()
    for l in data:
        l = l.strip()
        if not l:
            continue
        if l == "@startuml":
            uml = True
            continue
        if not uml:
            continue
        if l == "--":
            continue
        i = l.split()
        fname = i[0]
        pk = False
        if fname[0] in ("+", "#"):
            if fname[0] == "#":
                pk = True
            fname = fname[1:]
        if l == "@enduml":
            uml = False
            continue
        if not uml:
             continue
        if l.startswith("class"):
            table = True; field = False
            primary = []
            tab_name = tmap[i[1]]
            print("CREATE TABLE %s (" % tab_name)
            continue
        if table and not field and l == "==":
            field = True
            continue
        if field and l == "}":
            table = False; field = False
            print("\tCONSTRAINT pk_%s PRIMARY KEY(%s)" % (tab_name, ", ".join(primary)), end="")
            print("\n);\n")
            continue
        if field:
            col_def = cmap[fname]
            print("\t%s," % col_def)
        if field and pk:
            primary.append(cmap[fname].split(" ")[0])


if __name__ == "__main__":
    main()
