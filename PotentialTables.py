# Table candidates:

# Input: csv of (pdfUrl)
# Output: csv of (pdfUrl, name, pdfFile, page, candidateNo, candidateCoordinates, candidateImgFile)
import sys
import util

def main(input):

	pdfUrls = util.load(input)
	

	# (pdfUrl, name) = readInput

	# (pdfUrl, name, pdfFile) = downloadPDFs(input)

	# (pdfUrl, name, pdfFile, page, pageFile) = splitPDFs(prev)

	# (pdfUrl, name, pdfFile, page, pageFile, charBoxFile) = getCharboxes(prev)

	# (pdfUrl, name, pdfFile, page, pageFile, candidateNo, candidateCoordinates) = getCandidateBox(prev)

	# (pdfUrl, name, pdfFile, page, pageFile, candidateNo, candidateBoxFile, candidateImgFile) = getCandidateImage(prev)

main(sys.argv[1])

	# split pdfs into images
	# 	save the images
	# 	return the data




	# find the potential tables
	# 	save these images
	# 	return the data (this is the final output)



