#!/usr/bin/python

import sys

oldId = None
numOcc = 0
words = dict()

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        print "error"
        continue

    thisId = data[0]

    if oldId and thisId != oldId:
        words[thisId] = numOcc
        numOcc = 0
    numOcc += 1
    oldId = thisId
if oldId:
    words[oldId] = numOcc

for index, sortedKey in enumerate(sorted(words, key = words.get, reverse = True)):
    if index < 10:
        print "{0}\t{1}".format(sortedKey,words[sortedKey]) # gives the values sorted by key
