# Example call: python CatPages.py train 2 5

from os import listdir, system
from os.path import isfile, join
import sys

RAW_PDF_DIR = 'rawPDFs'
HOG_DIR = 'HOG'
LABELS_DIR = 'Labels'
CHARACTER_BOX_DIR = 'CharacterBoxes'

batch, name, numPages = sys.argv[1:]
featFiles = []
labelFiles = []
for page in range(1,int(numPages)+1):
	# featFile = "{}/{}-{}-page-{}-{}.csv".format(HOG_DIR, batch, name, page, HOG_DIR)
	labelFile = "{}/{}-{}-page-{}-{}.csv".format(LABELS_DIR, batch, name, page, LABELS_DIR)
	# print featFile
	# featFiles.append(featFile)
	labelFiles.append(labelFile)

# featCatCmd = " > features.csv".format(" ".join(featFiles))
labelCatCmd = "cat {} > labels.csv".format(" ".join(labelFiles))
# print labelCatCmd
# system(featCatCmd)
system(labelCatCmd)