from os import listdir, system
from os.path import isfile, join
import sys

RAW_PDF_DIR = 'rawPDFs'
BOUNDING_BOX_DIR = 'BoundingBoxes'

name = sys.argv[1]
numPages = int(sys.argv[2])

for page in range(0,numPages):
	cmd = "python TableCandidates.py {} {} > {}/{}-page-{}-boundingBoxes.csv".format(name, page, BOUNDING_BOX_DIR, name, page)
	system(cmd)
