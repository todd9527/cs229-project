"""
output: save as [name]-page[page]-candidates.csv
"""



import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import rank_filter
# import util



PAGE_IMAGES_DIR = 'pdfPages'
BOUNDING_BOX_DIR = 'boundingBoxes'
WIDTH_MAX = 50
HEIGHT_MAX = 50
WIDTH_MIN = 1
HEIGHT_MIN = 2

def getCountours(img):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
	contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	# contours, _ = cv2.findContours(cv2.adaptiveThreshold(img, 255, 1, 1, 11, 2), 
	# 	cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	return contours

# im = cv2.imread('pitrain.png') im3 = im.copy() gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) blur = cv2.GaussianBlur(gray,(5,5),0) thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2) ################# Now finding Contours ################### contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) samples = np.empty((0,100)) responses = [] keys = [i for i in range(48,58)] for cnt in contours: if cv2.contourArea(cnt)>50: [x,y,w,h] = cv2.boundingRect(cnt)

	contours, _ = cv2.findContours(cv2.adaptiveThreshold(img, 255, 1, 1, 11, 2), 
		cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	return contours

def getBoundingBox(contour):
	potential_bounding_box = cv2.boundingRect(contour) 
	x, y, w, h = potential_bounding_box
	return x, y, w, h

def isCharacterSized(w,h):
	return (w < WIDTH_MAX and h < HEIGHT_MAX and w > WIDTH_MIN and h > HEIGHT_MIN)

def getCharacterBoundingBoxes(img):
	bounding_boxes = []
	contours = getCountours(img)
	for contour in contours:
		bb = getBoundingBox(contour)
		x,y,w,h = bb
		if isCharacterSized(w,h):
			bounding_boxes.append(bb)
	return bounding_boxes



name = sys.argv[1]
page = sys.argv[2]

pageFile = "{}/{}-page-{}.jpg".format(PAGE_IMAGES_DIR, name, page)
img = cv2.imread(pageFile)

# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# display
# ef showImage(imgfile, color=None, boundingBoxes=None, points=None, bbColor=(200,0,0)):
# 	img = cv2.imread(imgfile)#, cv2.IMREAD_GRAYSCALE) #actually change the color scheme
# 	if boundingBoxes is not None:
# 		for bb in boundingBoxes:
# 			x,y,w,h = bb
# 			cv2.rectangle(img, (x,y), (x+w, y+h), bbColor,1)
# 	if points is not None:
# 		for point in points:
# 			x,y = point
# 			cv2.circle(img, (x,y), 3, (0, 255, 0), -1)

	# cv2.imshow('image',img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()

characterBoxes = getCharacterBoundingBoxes(img)
for bb in characterBoxes:
	x,y,w,h = bb
	cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# for x in characterBoxes:
# 	print x

# characterBoxes = bc.getCharacterBoundingBoxes('{}/{}'.format(PDF_PAGES_DIR,page['filename']))

#######################

# import sys


# infile = sys.argv[1]




	