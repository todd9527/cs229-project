import cv2
import sys 
import csv
#import model 
import numpy as np

IMG_DIR = 'pdfPages'
BBOX_DIR = 'BoundingBoxes'
LABEL_DIR = 'Labels'

def resize_image(image):
	temp_img = np.array(cv2.resize(image, (IMG_HEIGHT, IMG_WIDTH)))
	return np.reshape(temp_img, (IMG_HEIGHT, IMG_WIDTH, 1))

# Returns (X, Y) for training/testing with ML algorithm 
def prepare_data(batch, name, page_number): 
	cropped_images = []
	labels = [] 
	# for page_number in range(1, num_pages + 1):
	# Add all cropped images 
	full_image = cv2.imread('{}/{}-{}-page-{}.jpg'.format(IMG_DIR, batch, name, page_number), cv2.IMREAD_GRAYSCALE)
	# print batch, name, page_number
	#print np.shape(full_image)
	# break 
	# cv2.imshow('image',full_image)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()


	with open('{}/{}-{}-page-{}-{}.csv'.format(BBOX_DIR, batch, name, page_number, BBOX_DIR), 'rb') as ifile:
		readerx = csv.reader(ifile, delimiter=' ')
		for row in readerx:
			if row != []:
				row = [int(r) for r in row]
				xmin, xmax, ymin, ymax = tuple(row)
				#print row
				# if xmin >= xmax or ymin >= ymax:
				# 	print "Predict break here"
				# else:
				# 	print "No break predicted"
				cropped_img = full_image[ymin:ymax+1, xmin:xmax+1]
				#print cropped_img
				# cv2.imshow('image',cropped_img)
				# cv2.waitKey(0)
				# cv2.destroyAllWindows()
				cropped_images.append(resize_image(cropped_img))
	# Add all labels 
	with open('{}/{}-{}-page-{}-{}.csv'.format(LABEL_DIR, batch, name, page_number, LABEL_DIR), 'rb') as ifile2:
		readx = csv.reader(ifile2)
		#print readx
		ignore_line = True
		for curr_row in readx:
			if ignore_line:
				ignore_line = False
				continue
			if curr_row != []:
				curr_row = [int(float(r)) for r in curr_row]
				labels.append(curr_row[0])
	return (cropped_images, labels)
