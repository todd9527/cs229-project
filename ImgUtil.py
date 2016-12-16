# Nice.py
# The purpose of this file is to build a library for image proprocessing:
# DRY

import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import rank_filter
import csv
from sklearn import metrics
from sklearn import cluster 
import util
import math
import copy as cp

WIDTH_MAX = 50
HEIGHT_MAX = 50
WIDTH_MIN = 5
HEIGHT_MIN = 5
REDACTY_RED = (30,40,150)
GREEN = (0,255,0)
BLUE = (255,0,0)
MARGIN = 1



def display(img):
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

"""
Find the character boxes
"""
def isCharacterSized(box): 
	x1,y1,x2,y2 = box
	w = abs(x2-x1)
	h = abs(y2-y1)
	return (w < WIDTH_MAX and h < HEIGHT_MAX and w > WIDTH_MIN and h > HEIGHT_MIN)

def getContourBoxes(img):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
	contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	boxes = [cv2.boundingRect(contour) for contour in contours] #x,y,w,h form
	boxes = [(x,y,x+w,y+h) for x,y,w,h in boxes] #x1,y2,x2,y2 form
	return boxes

def addBoxes(img,boxes,color=GREEN,thickness=1):
	img2 = cp.deepcopy(img)
	for c in boxes:
		x,y,x2,y2 = c
		cv2.rectangle(img2, (x,y),(x2,y2), color,thickness)
	return img2

def getCharacterBoxes(img):
	charBoxes = getContourBoxes(img)
	#get rid of lines, images, anything that isn't about the structure of the text
	charBoxes = [c for c in charBoxes if isCharacterSized(c)]
	#add margins - beef the boxes up more so they'll be more likely to overlap
	charBoxes = [(x1-MARGIN,y1, x2+MARGIN,y2) for x1,y1,x2,y2 in charBoxes]
	return charBoxes


def redact(img):
	charBoxes = getCharacterBoxes(img)
	redacted = addBoxes(img, charBoxes, color=REDACTY_RED, thickness=-1)
	return redacted


def applyFilter(img):
	redacted = redact(img)
	RedFilter = ([17, 15, 100], [50, 56, 200])
	lower, upper = RedFilter
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")
	mask = cv2.inRange(redacted, lower, upper)
	blockified = cv2.bitwise_and(redacted, redacted, mask = mask)
	return blockified

# img = cv2.imread("pdfPages/train-1-page-61.jpg")
# display(img)

# withCharacterBoxes = addBoxes(img, getCharacterBoxes(img), thickness=1)
# display(withCharacterBoxes)

# redacted = redact(img)
# display(redacted)

# filtered = applyFilter(img)
# display(filtered)

# im1 = filtered

# blocks1 = getContourBoxes(im1)
# im2 = addBoxes(filtered, blocks1, thickness=-1)
# display(im2)

# blocks2 = getContourBoxes(im2)
# im3 = addBoxes(im2, blocks2, thickness=3)


# # print len(final)
# display(im3)

def blockify(img):
	blocks = getContourBoxes(img)
	return addBoxes(img, blocks, thickness=-1)

# toSave = blockify(filtered)

# display(toSave)

# boxes = getContourBoxes(toSave)
# points = np.array([((x1+x2)/2, (y1+y2)/2, (x2-x1)*(y2-y1)) for x1,y1,x2,y2 in boxes])

"""
# The next part is about k-mean clustering
# input: blockBoxes
i'm testing this out for only one value of k
"""

# get their center x,y and areas as coordinates
# assignments = np.zeros(len(points))
# print assignments
# assignments = np.zeros((MAX_CLUSTERS + 1, len(character_locations)))
# silhouette_scores = [0] * (MAX_CLUSTERS + 1)  # Best value is 1, worst value is -1 

# k = 3
# silhouette_scores = [0] * (MAX_CLUSTERS + 1)  # Best value is 1, worst value is -1 

# kmeans_result =  cluster.KMeans(n_clusters = k, max_iter = 30).fit(points.reshape(-1, 1))

"""
Note to self - when you wake up, you mission is to:
Re-implement k-means algorithm for the redacted/blockified image - currently named 'toSave'
(it might just be a matter of using Todd's code [almost] as is)
As soon as you've finished that
set up the pipeline
Write it all up

"""

# assignments = kmeans_result.labels_
# centroids = kmeans_result.cluster_centers_
# print assignments

# blueBoxes = []
# for i in range(0,len(points)+1):
# 	if assignments[i] == 2:
# 		blueBoxes.append(final[i])

# display(addBoxes(finalImg, blueBoxes, color=BLUE, thickness = -1))

# print centroids
# assignments[num_clusters, :] = kmeans_result.labels_
# centroids = kmeans_result.cluster_centers_
# print centroids

# indexes = np.array(silhouette_scores).argsort()[::-1]





"""
For when you're doing feature descriptors
"""
# Harris corner detection
# gray = cv2.cvtColor(toSave,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
# toSave[dst>0.01*dst.max()]=[0,0,255]
"""
"""











# cv2.imshow("images", np.hstack([img, output])) #this is how you show multiple images
