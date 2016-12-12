#!/usr/bin/python
import os
import sys
import csv
import urllib


filename = sys.argv[1]
n = 0
with open(filename, 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	n+=1
    	pdfNumber = reader.line_num-1
    	url = row['url']
    	cmd = "python download.py {} {}".format(pdfNumber, url)
    	os.system(cmd)
print n
