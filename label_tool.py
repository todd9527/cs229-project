import cv2
import sys 
import csv
import numpy as np
from sklearn import metrics
from sklearn import cluster 
from matplotlib import pyplot as plt

# def compute_subimages():
OUTPUT_FILE_PREFIX = 'labels-'

if len(sys.argv) != 4:
	raise Exception('Please provide 3 args')

img_filename = sys.argv[1]
bounding_boxes_filename = sys.argv[2]
num_pages = int(sys.argv[3])

for i in range(1, num_pages + 1):
	cropped_images = image_util.crop_image(img_filename + str(i) + '.jpg', 
			bounding_boxes_filename + str(i) + '.csv')

	with open(OUTPUT_FILE_PREFIX + str(i) + '.csv', 'w') as ofile: 
		for cropped_image in cropped_images:
			label