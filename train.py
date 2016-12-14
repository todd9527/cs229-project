#Input params: <batch> <name> <num_pages>

import sys 
import model
import model_util 

def main():
	# if len(sys.argv) != 4:
	# 	return
	# batch = sys.argv[1]
	# name = sys.argv[2]
	# num_pages = int(sys.argv[3])

	#cropped_images, labels = model_util.prepare_data(batch, name, num_pages)
	#print cropped_images[0], labels[0]
	#print len(cropped_images), len(labels)
	# cnn_model = model.CNN_Model()
	# cnn_model.train_model(cropped_images, labels)
	# cnn_model = model.CNN_Model()
	# cnn_model.train_model([], [])


#**********FOR SIFT FEATURES**************
	# sift = cv2.xfeatures2d.SIFT_create()
 #    2 kp, des = sift.detectAndCompute(gray,None)

 #     import cv2
 #    2 import numpy as np
 #    3 
 #    4 img = cv2.imread('home.jpg')
 #    5 gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 #    6 
 #    7 sift = cv2.xfeatures2d.SIFT_create()
 #    8 kp = sift.detect(gray,None)
 #    9 
 #   10 img=cv2.drawKeypoints(gray,kp)
 #   11 
 #   12 cv2.imwrite('sift_keypoints.jpg',img)
#********************************************

#***********FOR HOG FEATURES*******************
# import cv2
# image = cv2.imread("test.jpg",0)
# winSize = (64,64)
# blockSize = (16,16)
# blockStride = (8,8)
# cellSize = (8,8)
# nbins = 9
# derivAperture = 1
# winSigma = 4.
# histogramNormType = 0
# L2HysThreshold = 2.0000000000000001e-01
# gammaCorrection = 0
# nlevels = 64
# hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins,derivAperture,winSigma,
#                         histogramNormType,L2HysThreshold,gammaCorrection,nlevels)
# #compute(img[, winStride[, padding[, locations]]]) -> descriptors
# winStride = (8,8)
# padding = (8,8)
# locations = ((10,20),)
# hist = hog.compute(image,winStride,padding,locations)
#**********************************************
	





if __name__ == "__main__":
    main()
