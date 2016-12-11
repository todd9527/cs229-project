# main.py
import util
import BoundCharacters as bc


# Take in list of pdf URLs - save to local folder
pdfURLs = util.csvToList("pdfURLs.csv")
pdfs = [{'name': 'pdf{}'.format(ind), 'url': x['url'], 'path': "rawPDFs/pdf{}".format(ind)} for ind, x in enumerate(pdfURLs)]

for pdf in pdfs:
	util.getPdfFromURL(pdf['url'], pdf['path'])
	


print pdfs
# pdfs = { p.id : {'id': p.id, 'position': ind} for ind, p in enumerate(p_list)}

# pdfs = [{""}
# "pdf{}".format(i) for i in xrange(urls)]
# print pdfURLs
# pdfNames = 



# To show the bounding boxes for characters on a sample image
# bbs = bc.getCharacterBoundingBoxes("myDir/testing-23.jpg")
# util.showBoundingBoxes("myDir/testing-23.jpg", bbs)