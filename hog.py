import cv2
import model_util
import sys 

OUTPUT_DIR = 'HOG'
IMG_DIR = 'pdfPages'

# batch name page 

def main():
	if len(sys.argv) != 4:
		return
	batch = sys.argv[1]
	name = sys.argv[2]
	page_num = int(sys.argv[3])

	# HOG constants 
	winSize = (64,64)
	blockSize = (16,16)
	blockStride = (8,8)
	winStride = (8,8)
	padding = (8,8)
	cellSize = (8,8)
	nbins = 9

	cropped_images, labels = model_util.prepare_data(batch, name, page_num)
	hog = cv2.HOGDescriptor(winSize,blockSize,blockStride,cellSize,nbins)
	for cropped_image in cropped_images: 
		print hog.compute(cropped_image, winStride, padding)



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

