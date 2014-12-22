#!/usr/bin/python

import sys

oldThread = None
students = []

for line in sys.stdin:
    data = line.strip().split('\t')

    if len(data) != 2:
        print "error"
        continue

    thisThread, thisStudent = data

    if oldThread and thisThread != oldThread:
        print "{0}\t{1}".format(oldThread, students)
        students = []
    oldThread = thisThread
    students.append(thisStudent)

if oldThread:
    print "{0}\t{1}".format(oldThread, students)
