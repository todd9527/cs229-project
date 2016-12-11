# Useful functions that will be used across our codebase
import urllib
import os



# Takes in a url or path, spits out a name
def getPdfFromURL(url, name):
	pdfName = "{}.pdf".format(name)
	file = urllib.URLopener()
	file.retrieve(url, pdfName)

"""
Input: example.pdf
Output: example-i.jpg (i = 1->#pages)
Requires working imagemagick - which means this will probably only work on Nick's computer
"""
def splitPDF(name):
	cmd = "convert {}.pdf myDir/{}.jpg".format(name, name)
	os.system(cmd)


"""
Given a csv containing the coordinates of each bounding box and an image,
show those bounding boxes on original image
"""
# def showBoundingBoxes(imgPath, bbPath):

