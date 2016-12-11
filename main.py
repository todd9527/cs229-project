# main.py
import os
import util
import BoundCharacters as bc
import re

RAW_PDF_DIR = 'rawPDFs'
PDF_PAGES_DIR = 'pdfPages'


# Take in list of pdf URLs - save to local folder
pdfURLs = util.csvToList("pdfURLs.csv")
pdfs = [{'name': 'pdf{}'.format(ind), 'url': x['url'], 'path': "{}/pdf{}".format(RAW_PDF_DIR,ind)} for ind, x in enumerate(pdfURLs)]

for pdf in pdfs:
	name = pdf['name']
	# util.getPdfFromURL(pdf['url'], pdf['path']) #You can comment this out to save time

	# util.splitPDF(name, RAW_PDF_DIR, PDF_PAGES_DIR)  #You can comment this out to save time
	# works up to here
	pages = [{'filename':filename, 'pgNum': int(re.split("\.|\-", filename)[1])} for filename in os.listdir('./{}'.format(PDF_PAGES_DIR)) if filename.startswith(name)]
	pages.sort(key = lambda x: x['pgNum'])

	for page in pages:
		
		print page
	# print pages
	# sort by page number
	# pdf0-0.jpg

	# how do I for loop through the pdf pages
# 	import os
# for file in os.listdir("/mydir"):

#     if file.endswith(".txt"):
#         print(file)

	




# print pdfs
# pdfs = { p.id : {'id': p.id, 'position': ind} for ind, p in enumerate(p_list)}

# pdfs = [{""}
# "pdf{}".format(i) for i in xrange(urls)]
# print pdfURLs
# pdfNames = 



# To show the bounding boxes for characters on a sample image
# bbs = bc.getCharacterBoundingBoxes("myDir/testing-23.jpg")
# util.showBoundingBoxes("myDir/testing-23.jpg", bbs)