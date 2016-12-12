# splits all pdfs
# output: number of pages for each pdf

from os import listdir, system
from os.path import isfile, join
import re
import sys

RAW_PDF_DIR = 'rawPDFs'

batch = sys.argv[1]

onlyfiles = [f for f in listdir(RAW_PDF_DIR) if isfile(join(RAW_PDF_DIR, f))]
pdfFileNames = [f.split(".")[0] for f in onlyfiles if f.endswith('.pdf')]
pdfNames = [f.split("-")[2] for f in pdfFileNames]


for name in pdfNames:
	cmd = "python split.py {} {}".format(batch, name)
	system(cmd)
