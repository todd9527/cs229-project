#!/usr/bin/python
import os
import sys
import urllib

RAW_PDF_DIR = 'rawPDFs'


name = sys.argv[1]
url = sys.argv[2]
pdfName = "{}/pdf-{}.pdf".format(RAW_PDF_DIR, name)
file = urllib.URLopener()
file.retrieve(url, pdfName)

