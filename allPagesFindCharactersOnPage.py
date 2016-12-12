from os import listdir, system
from os.path import isfile, join
import sys

RAW_PDF_DIR = 'rawPDFs'
CHARACTER_BOX_DIR = 'CharacterBoxes'

name = sys.argv[1]
numPages = int(sys.argv[2])

for page in range(1,numPages+1):
	cmd = "python FindCharactersOnPage.py {} {} > {}/{}-page-{}-{}.csv".format(name, page, CHARACTER_BOX_DIR, name, page, CHARACTER_BOX_DIR)
	system(cmd)
