# Useful functions that will be used across our codebase
import urllib



# Takes in a url or path, spits out a name
def getPdfFromURL(url, name):
	pdfName = "{}.pdf".format(name)
	file = urllib.URLopener()
	file.retrieve(url, pdfName)
	return pdfName

"""
Given a csv containing the coordinates of each bounding box and an image,
show those bounding boxes on original image
"""
# def showBoundingBoxes(imgPath, bbPath):

