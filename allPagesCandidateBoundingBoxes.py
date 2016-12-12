from os import listdir, system
from os.path import isfile, join
import sys

PAGES_DIR = 'pdfPages'
BOUNDING_BOX_DIR = 'BoundingBoxes'
CHARACTER_BOX_DIR = 'CharacterBoxes'

batch, name, numPages = sys.argv[1:]
numPages = int(numPages)


for page in range(1,numPages+1):
	# print batch, name, page
	cmd = "python candidateBoundingBoxes.py {} {} {} > {}/{}-{}-page-{}-{}.csv".format(batch, name, page, BOUNDING_BOX_DIR, batch, name, page, BOUNDING_BOX_DIR)
	system(cmd)
