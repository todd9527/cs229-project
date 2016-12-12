from os import listdir, system
from os.path import isfile, join
import sys

RAW_PDF_DIR = 'rawPDFs'
CHARACTER_BOX_DIR = 'CharacterBoxes'

batch, name, numPages = sys.argv[1:]
numPages = int(numPages)


for page in range(1,numPages+1):
	# print batch, name, page
	cmd = "python FindCharactersOnPage.py {} {} {} > {}/{}-{}-page-{}-{}.csv".format(batch, name, page, CHARACTER_BOX_DIR, batch, name, page, CHARACTER_BOX_DIR)
	system(cmd)
