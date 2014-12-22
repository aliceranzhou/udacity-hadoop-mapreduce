#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if line[0] != "id":
        if len(line) != 19:
            continue
        tagnames = line[2].strip().split();
        node_type = (line[5]).lower()
        if node_type == "question":
            for tag in tagnames:
                print "{0}\t{1}".format(tag, "1")
