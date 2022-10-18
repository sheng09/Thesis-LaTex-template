#!/usr/bin/env python3
from pybtex.database.input import bibtex

items = ('url', 'urldate', 'note', 'abstract', 'note', 
            'file', 'keywords', 'langid')

parser = bibtex.Parser()
bib_data = parser.parse_file('SW-biblatex.bib.raw')
bib_data.entries.keys()

for k, v in bib_data.entries.items():
    for junkk in items:
        try:
            v.fields.pop(junkk)
        except Exception:
            pass
    try:
        tmp = v.fields['date']
        v.fields['date'] = '-'.join(tmp.split('-')[:2])
    except Exception:
        pass
    #for fk, fv in v.fields.items():
    #    print(fk, fv)
    #pass
bib_data.to_file('SW-biblatex.bib', bib_format='bibtex')
#
#items = ('note', )
#with open('SW-biblatex.bib', 'w') as oid:
#    with open('SW-biblatex.bib.raw', 'r') as #fid:
#        for line in fid:
#            jumpflag = False
#            if '=' in line:
#                for it in items:
#                    if it in line.split()[0]:
#                        jumpflag = True
#                        continue
#            if not jumpflag:
#                print(line, end='', file=oid)