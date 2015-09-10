# -*- encoding: utf-8 -*-
import re
import codecs
import csv
fi = codecs.open('prosym_formatted.txt', 'r', 'utf-8')
writer = csv.writer(file('prosym_title.csv', 'w'))
writer2 = csv.writer(file('prosym_affiliation.csv', 'w'))

def to_utf8(*xs):
    return [x.encode('utf-8') for x in xs]

title = ''
for line in fi:
    print line.strip()
    if line.startswith('!'):
        continue
    if line.startswith('##'):
        items = line.strip().split()
        #print items
        _tag, event, start, _tag, _end = items
        event = event + u'プログラミングシンポジウム'
    elif line.startswith('#'):
        items = line.strip().split(' ', 1)
        #print line
        #print items
        _tag, title = items
    elif title:
        assert re.match('([^,()]+) \(([^()]*)\)(, ([^,()]+) \(([^()]*)\))*$', line)
        items = re.findall('([^,()]+) \(([^()]*)\)', line)
        for item in items:
            name, affil = item
            name = name.strip()
            writer.writerow(to_utf8(name, event, title, start))
            for a in affil.split(','):
                writer2.writerow(to_utf8(name, a.strip(), start))
        #print line
        #print items

        title = ''
    #print line
