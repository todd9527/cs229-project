import sys
import csv
import urllib
import os
import numpy as np
import cv2

# filename = sys.argv[1]
filename = 'pdfPages/pdf0-4.jpg'
img = cv2.imread(filename,0)
cv2.imshow('image',img)

k = cv2.waitKey(0)
if k == ord('q'):
	print 0  
elif k == ord('w'):
	print 1

cv2.destroyAllWindows()



