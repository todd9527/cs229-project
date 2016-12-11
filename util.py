# Useful functions that will be used across our codebase
import csv
import urllib
import os
import cv2


def csvToList(file):
	with open(file) as csvfile:
	    reader = csv.DictReader(csvfile)
	    res = [row for row in reader]
    	return res


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
Given an image fileName, display it
Optional: display with bounding boxes
"""
def showImage(imgfile, color=None, boundingBoxes=None, bbColor=None):
	img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE) #actually change the color scheme
	if boundingBoxes is not None:
		for bb in boundingBoxes:
			x,y,w,h = bb
			cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),1)
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
