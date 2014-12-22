#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
for line in reader:
    if line[0] != "id":
        if len(line) != 19:
            continue
        post_id = line[0]
        body = line[4]
        length = len(body)
        node_type = (line[5]).lower()
        if node_type == "question" or node_type == "answer":
            print "{0}\t{1}\t{2}".format(post_id, node_type, length)
