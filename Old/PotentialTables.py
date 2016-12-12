# Table candidates:

# Input: csv of (pdfUrl)
# Output: csv of (pdfUrl, name, pdfFile, page, candidateNo, candidateCoordinates, candidateImgFile)
import sys
import util

def main(input):

	# (pdfUrl, name) = readInput
	pdfUrls = util.load(input)

	function for updating dictionary
	util.addField(pdfUrls, key="name")
	key, function to get value

    item.update( {"elem":"value"})

	I need to add data
	list2 = [(x,ind) for x, ind in enumerate(foo)]

	pdfs = [{'name': 'pdf{}'.format(ind), 'url': x['url'], 'path': "{}/pdf{}".format(RAW_PDF_DIR,ind)} for ind, x in enumerate(pdfURLs)]

	# (pdfUrl, name, pdfFile) = downloadPDFs(input)
	# pdfs = [downloadPDF(x) for x in pdfUrls]


	# (pdfUrl, name, pdfFile, page, pageFile) = splitPDFs(prev)

	# (pdfUrl, name, pdfFile, page, pageFile, charBoxFile) = getCharboxes(prev)

	# (pdfUrl, name, pdfFile, page, pageFile, candidateNo, candidateCoordinates) = getCandidateBox(prev)

	# (pdfUrl, name, pdfFile, page, pageFile, candidateNo, candidateBoxFile, candidateImgFile) = getCandidateImage(prev)

# input: 
def downloadPDF(pdf):


main(sys.argv[1])

	# split pdfs into images
	# 	save the images
	# 	return the data




	# find the potential tables
	# 	save these images
	# 	return the data (this is the final output)



