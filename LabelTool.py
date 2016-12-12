import sys
import csv
import urllib
import os
import numpy as np
import cv2

# filename = sys.argv[1]
def handLabel(img):
	label = 0
	cv2.imshow('image',img)
	k = cv2.waitKey(0)
	if k == ord('q'):
		label = 0  
	elif k == ord('w'):
		label = 1
	cv2.destroyAllWindows()
	return label



# filename = 'pdfPages/pdf0-4.jpg'
# img = cv2.imread(filename,0)


# k = cv2.waitKey(0)
# if k == ord('q'):
# 	print 0  
# elif k == ord('w'):
# 	print 1




