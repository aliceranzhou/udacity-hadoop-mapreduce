#!/usr/bin/python

import sys

oldId = None
questionLength = 0
sumAnswer = 0
numAnswer = 0
avgAnswer = 0

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 3:
        print "error"
        continue

    thisId, nodeType, length = data
    length = int(length)
    
    if oldId and thisId != oldId:

        if questionLength != 0:
            if 0 == numAnswer:
                print "{0}\t{1}\t{2}".format(oldId,questionLength,0)
            else:
                print "{0}\t{1}\t{2}".format(oldId,questionLength,float(sumAnswer/numAnswer))
        sumAnswer = 0
        numAnswer = 0
        questionLength = 0

    if nodeType == "question":
        questionLength = length
    elif nodeType == "answer":
        sumAnswer += length
        numAnswer += 1

    oldId = thisId
    print numAnswer
    print sumAnswer

if oldId:
    avgAnswer = 0
    if numAnswer != 0:
        avgAnswer = float(sumAnswer)/float(numAnswer)
    print "{0}\t{1}\t{2}".format(oldId,questionLength,avgAnswer)
