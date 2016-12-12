from os import listdir, system
from os.path import isfile, join
import sys
import csv

batch = sys.argv[1]
batchPageCountFile = "{}-pagesPerPDF.csv".format(batch)
with open(batchPageCountFile, 'r') as csvfile:
	reader = csv.reader(csvfile)
	name = 0
	for row in reader:
		name = name+1
		numPages = row[0]
		cmd = "python allPagesCandidateBoundingBoxes.py {} {} {}".format(batch, name, numPages)
		system(cmd)

