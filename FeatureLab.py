# FeatureDetectLab.py

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

WIDTH_MAX = 50
HEIGHT_MAX = 50
WIDTH_MIN = 1
HEIGHT_MIN = 2

# # img = cv2.imread("Table_For_Feature_detection.jpg")
# # img = cv2.imread("pdfPages/train-1-page-22.jpg")
img = cv2.imread("text.jpg")


def display(img):
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def isCharacterSized(box):
	return (w < WIDTH_MAX and h < HEIGHT_MAX and w > WIDTH_MIN and h > HEIGHT_MIN)


display(img)
"""
Find the contours
"""
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

charBoxes = [cv2.boundingRect(contour) for contour in contours]
charBoxes = [c for c in charBoxes if isCharacterSized(c)]
for c in charBoxes:
	x,y,w,h = c
	x2 = x+w
	y2 = y+h
	cv2.rectangle(img, (x,y),(x2,y2), (0,255,0), 3)

display(img)
