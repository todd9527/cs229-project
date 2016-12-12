
"""
Input: example.pdf
Output: [name]-page[page].jpg
Requires working imagemagick - which means this will probably only work on Nick's computer
"""


import sys
import os

RAW_PDF_DIR = 'rawPDFs'
PAGE_IMAGES_DIR = 'pdfPages'

name = sys.argv[1]
cmd = "convert {}/pdf{}.pdf {}/{}-page.jpg".format(RAW_PDF_DIR, name, PAGE_IMAGES_DIR, name)
os.system(cmd)

