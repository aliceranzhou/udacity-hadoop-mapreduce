#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if line[0] != "id":
        if len(line) != 19:
            continue
        thread = line[0] 
        student = line[3]
        print "{0}\t{1}".format(thread, student)
