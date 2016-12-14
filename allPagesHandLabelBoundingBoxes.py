from os import listdir, system
from os.path import isfile, join
import sys

LABELS_DIR = "Labels"

batch, name, numPages = sys.argv[1:]
numPages = int(numPages)


for page in range(1,numPages+1):
	# print batch, name, page
	batch, name, page = sys.argv[1:]
	cmd = "python handLabelBoundingBoxes.py {} {} {} > {}/{}-{}-page-{}-{}.csv".format(batch, name, page, LABELS_DIR, batch, name, page, LABELS_DIR)
	system(cmd)
