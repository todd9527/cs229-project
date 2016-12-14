import cv2
import model_util
import sys 

OUTPUT_DIR = 'SIFT'
IMG_DIR = 'pdfPages'

# batch name page 

def main():
	if len(sys.argv) != 4:
		return
	batch = sys.argv[1]
	name = sys.argv[2]
	page_num = int(sys.argv[3])

	cropped_images, labels = model_util.prepare_data(batch, name, page_num)
	sift = cv2.SIFT()
	for cropped_image in cropped_images: 
		# gray_image = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2GRAY)
		key_points, descriptors = sift.detectAndCompute(cropped_image,None)
		print descriptors




if __name__ == "__main__":
    main()


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