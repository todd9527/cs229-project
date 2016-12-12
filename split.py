
"""
Input: example.pdf
Output: [name]-page[page].jpg
Requires working imagemagick - which means this will probably only work on Nick's computer
"""


import sys
import os
import pyPdf

RAW_PDF_DIR = 'rawPDFs'
PAGE_IMAGES_DIR = 'pdfPages'

name = sys.argv[1]
path = "{}/pdf-{}.pdf".format(RAW_PDF_DIR, name)
cmd = "convert {} {}/{}-page.jpg".format(path, PAGE_IMAGES_DIR, name)
os.system(cmd)

# Hacky way of counting pages
reader = pyPdf.PdfFileReader(open(path))
print reader.getNumPages() 

