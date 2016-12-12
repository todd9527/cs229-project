from os import listdir, system
from os.path import isfile, join
import sys
import LabelTool
import util
import cv2
import csv

IMG_DIR = "pdfPages"
BOUNDING_BOX_DIR = 'BoundingBoxes'
LABEL_DIR = 'labels'

def classify(img):
	return 0
	
name = sys.argv[1]
# page = sys.argv[2]
pages = int(sys.argv[2])

for page in range(1, pages + 1):
	imageFile = "{}/{}-page-{}.jpg".format(IMG_DIR,name,page)
	boundingBoxFile = "{}/{}-page-{}-{}.csv".format(BOUNDING_BOX_DIR,name,page, BOUNDING_BOX_DIR)
	labelsFile = "{}/{}-page-{}-{}.csv".format(LABEL_DIR,name,page, LABEL_DIR)
	wholePageImg = cv2.imread(imageFile,0)

	labels = []

	with open(boundingBoxFile, 'rb') as csvfile:
	    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	    for row in reader:
	    	row = [int(a) for a in row]
	    	x,y,w,h = row
	    	#print x,y,w,h
	    	crop_img = wholePageImg[x:x+w, y:y+h]
	    	labels.append(LabelTool.handLabel(crop_img))
	with open(labelsFile, 'w') as outfile:
		writer = csv.writer(outfile)
		for label in labels:
			writer.writerow([label])




	    	# img = w
	    	# print classify(img)




