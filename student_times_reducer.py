#!/usr/bin/python

import sys

d = [0]*24
oldId = None

def printer():
    maxValue = max(d)
    for index, i in enumerate(d):
        if i==maxValue:
            print "{0}\t{1}".format(thisId,index)

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) != 2:
        print len(data)
        continue
    thisId, hour = data
    if oldId and thisId != oldId:
        printer()
        d = [0]*24
    oldId = thisId
    d[int(hour)] += 1
if oldId:
    printer()
