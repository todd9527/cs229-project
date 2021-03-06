"""
output: save as [name]-page[page]-candidates.csv
"""

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


PAGE_IMAGES_DIR = 'pdfPages'
CHARACTER_BOX_DIR = 'CharacterBoxes'
WIDTH_MAX = 50
HEIGHT_MAX = 50
WIDTH_MIN = 1
HEIGHT_MIN = 2
MAX_CLUSTERS = 3 # Maximum number of possible clusters per image 
SELECTED_CLUSTERS = 3 # Must be <= MAX_CLUSTERS 
OUTPUT_FILENAME = 'candidate_boxes_' # Do not include csv extension 


def getCountours(img):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(gray,(5,5),0)
	thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
	contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	# contours, _ = cv2.findContours(cv2.adaptiveThreshold(img, 255, 1, 1, 11, 2), 
	# 	cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	return contours

def getContourBox(contour):
	potential_bounding_box = cv2.boundingRect(contour) 
	x, y, w, h = potential_bounding_box
	return x, y, w, h

def isCharacterSized(w,h):
	return (w < WIDTH_MAX and h < HEIGHT_MAX and w > WIDTH_MIN and h > HEIGHT_MIN)

def getCharacterBoundingBoxes(img):
	bounding_boxes = []
	contours = getCountours(img)
	for contour in contours:
		bb = getContourBox(contour)
		x,y,w,h = bb
		if isCharacterSized(w,h):
			bounding_boxes.append(bb)
	return bounding_boxes

def getBoxCenterPoint(x,y,w,h):
	return (x + w/2, y + h/2)

def drawDot(img, x,y, color=None):
	cv2.circle(img, (x, y), 3, (0, 255, 0), -1)

def getPageTableCandidates(batch, name, page):
	pageFile = "{}/{}-{}-page-{}.jpg".format(PAGE_IMAGES_DIR, batch, name, page)
	img = cv2.imread(pageFile)
	# util.showImage(pageFile)
	characterBoxes = getCharacterBoundingBoxes(img)
	# util.showImage(pageFile, boundingBoxes=characterBoxes)
	for cb in characterBoxes:
		x,y,w,h = cb
		print "{},{},{},{}".format(x,y,w,h)

batch, name, page = sys.argv[1:]
getPageTableCandidates(batch, name, page)

