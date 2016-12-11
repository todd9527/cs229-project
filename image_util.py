import cv2
import sys 
import csv
import numpy as np
from sklearn import metrics
from sklearn import cluster 
from matplotlib import pyplot as plt

def crop_image(img_filename, bounding_boxes_filename):

	# Read both files and return a list of cropped images 
