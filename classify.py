from os import listdir, system
from os.path import isfile, join
import sys
import LabelTool
import util
import cv2

IMG_DIR = "pdfPages"

classifier = sys.argv[1]
name = sys.argv[2]
page = sys.argv[3]
x = int(sys.argv[4])
y = int(sys.argv[5])
w = int(sys.argv[6])
h = int(sys.argv[7])

filename = "{}/{}-page-{}.jpg".format(IMG_DIR,name,page)
img = cv2.imread(filename,0)
crop_img = img[x:x+w, y:y+h]
print(LabelTool.handLabel(crop_img))

# util.


# if classifier = "handlabel":


# 	print "woo"
# else:
# 	print("classifier {} is not implemented yet".format(classifier))


# This file is for taking in:
# 	name
# 	page

# 	spitting out labels


# 	cmd = "python TableCandidates.py {} {} > {}/{}-page-{}-boundingBoxes.csv".format(name, page, BOUNDING_BOX_DIR, name, page)
