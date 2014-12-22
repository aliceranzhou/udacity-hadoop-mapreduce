#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdin, delimiter='\t', quotechar='"',
        quoting=csv.QUOTE_ALL)
for line in reader:
    if line[0] != "id":
        if len(line) != 19:
            continue
        author_id = line[3]
        added_at = line[8]
        time = (added_at.split())[1]
        hour = time.strip().split(":")[0]
        if hour[0] == "0" and hour[1] != "0":
            hour = hour.translate(None, '0')
        print "{0}\t{1}".format(author_id,hour)
