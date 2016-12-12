# ViewBoundingBoxes.py

import util
import sys
import cv2
import csv

IMG_DIR = "pdfPages"

batch, name, page = sys.argv[1:4]


imgfile = "{}/{}-{}-page-{}.jpg".format(IMG_DIR, batch, name, page)

if len(sys.argv) > 4:
	boxDir = sys.argv[4]
	delimiter = sys.argv[5]


	boxfile = "{}/{}-{}-page-{}-{}.csv".format(boxDir, batch, name, page, boxDir)



	with open(boxfile, 'rb') as f:
		reader = csv.reader(f, delimiter=delimiter)
		box_list = [(int(p[0]),int(p[1]),int(p[2]),int(p[3])) for p in list(reader)]
		# print box_list

		# box_list = [(p[0], p[1], p[2], p[3]) for p in list(reader)]
		util.showImage(imgfile, boundingBoxes=box_list)

else:

	util.showImage(imgfile)

# img = cv2.imread(imgfile)#, cv2.IMREAD_GRAYSCALE) #actually change the color scheme
# img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# """
# Given an image fileName, display it
# Optional: display with bounding boxes
# """
# def showImage(imgfile, color=None, boundingBoxes=None, points=None, bbColor=(200,0,0)):
# 	img = cv2.imread(imgfile)#, cv2.IMREAD_GRAYSCALE) #actually change the color scheme
# 	if boundingBoxes is not None:
# 		for bb in boundingBoxes:
# 			xmin,xmax, ymin,ymax = bb
# 			cv2.rectangle(img, (xmin,ymin), (xmax, ymax), bbColor,1)
# 	if points is not None:
# 		for point in points:
# 			x,y = point
# 			cv2.circle(img, (x,y), 3, (0, 255, 0), -1)

# 	cv2.imshow('image',img)
# 	cv2.waitKey(0)
# 	cv2.destroyAllWindows()