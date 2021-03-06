# redact_text.py

import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import rank_filter

# infile = sys.argv[1]
WIDTH_MAX = 50
HEIGHT_MAX = 50
WIDTH_MIN = 1
HEIGHT_MIN = 2


def getCountours(img):
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
	contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) samples = np.empty((0,100)) responses = [] keys = [i for i in range(48,58)] for cnt in contours: if cv2.contourArea(cnt)>50: [x,y,w,h] = cv2.boundingRect(cnt)

	# contours, _ = cv2.findContours(cv2.adaptiveThreshold(img, 255, 1, 1, 11, 2), 
	# 	cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	return contours

# im = cv2.imread('pitrain.png') im3 = im.copy() gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY) blur = cv2.GaussianBlur(gray,(5,5),0) thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2) ################# Now finding Contours ################### contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) samples = np.empty((0,100)) responses = [] keys = [i for i in range(48,58)] for cnt in contours: if cv2.contourArea(cnt)>50: [x,y,w,h] = cv2.boundingRect(cnt)




def getBoundingBox(contour):
	potential_bounding_box = cv2.boundingRect(contour) 
	x, y, w, h = potential_bounding_box
	return x, y, w, h

def isCharacterSized(w,h):
	return (w < WIDTH_MAX and h < HEIGHT_MAX and w > WIDTH_MIN and h > HEIGHT_MIN)

def getCharacterBoundingBoxes(filename):
	bounding_boxes = []

	img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
	contours = getCountours(img)
	for contour in contours:
		bb = getBoundingBox(contour)
		x,y,w,h = bb
		if isCharacterSized(w,h):
			bounding_boxes.append(bb)
	return bounding_boxes

	



# for i in range(1, len(sys.argv)):
# 	img = cv2.imread(sys.argv[i], cv2.IMREAD_GRAYSCALE)
# 	print(img.shape)

# 	# Detect edges
# 	# edges = cv2.Canny(img,100,200)


# 	# Blur image 
# 	# blurred = cv2.GaussianBlur(edges, (5,5), 0)

# 	contours, _ = cv2.findContours(cv2.adaptiveThreshold(img, 255, 1, 1, 11, 2), 
# 		cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 	bounding_boxes = []

# 	print len(contours)
# 	for contour in contours:
# 		potential_bounding_box = cv2.boundingRect(contour) 
# 		x, y, w, h = potential_bounding_box
		

# 	# plt.imshow(img, cmap='gray')

# 		if w < WIDTH_MAX and h < HEIGHT_MAX and w > WIDTH_MIN and h > HEIGHT_MIN: 
# 			bounding_boxes.append(potential_bounding_box)
# 			cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0),2)

	

# 	print bounding_boxes


	# cv2.imshow('image',img)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()


	# plt.subplot(121),plt.imshow(img,cmap = 'gray')
	# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
	
	# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
	# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


	# # remove lines
	# blurred = cv2.GaussianBlur(edges, (5,5), 0)
	# plt.subplot(221),plt.imshow(blurred,cmap = 'gray')
	# plt.title('Blurred Image'), plt.xticks([]), plt.yticks([])


