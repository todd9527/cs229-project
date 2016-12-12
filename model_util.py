import cv2
import sys 
import csv
import model 
import numpy as np

IMG_DIR = 'pdfPages'
BBOX_DIR = 'BoundingBoxes'
LABEL_DIR = 'labels'

# Returns (X, Y) for training/testing with ML algorithm 
def prepare_data(batch, name, num_pages): 
	cropped_images = []
	labels = [] 
	for page_num in range(1, num_pages + 1):
		# Add all cropped images 
		full_image = cv2.imread('{}/{}-{}-page-{}-{}.jpg'.format(IMG_DIR, batch, pdf_number, page_number, IMG_DIR))
		with open('{}/{}-{}-page-{}-{}.jpg'.format(BBOX_DIR, batch, pdf_number, page_number, BBOX_DIR)), 'rb') as ifile:
			readerx = csv.reader(ifile)
			for row in readerx:
				xmin, xmax, ymin, ymax = row
				cropped_images.append(model.resize_image(full_image[int(xmin):int(xmax), int(ymin):int(ymax)]))
		# Add all labels 
		with open('{}/{}-{}-page-{}-{}.jpg'.format(LABEL_DIR, batch, pdf_number, page_number, LABEL_DIR)), 'rb') as ifile:
			readx = csv.reader(ifile)
			for row in readerx:
				labels.append(int(row[0]))
	return (cropped_images, labels)
