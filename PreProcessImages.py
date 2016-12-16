import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage.filters import rank_filter
import csv
from sklearn import metrics
from sklearn import cluster 
import util
import math
import copy as cp
import ImgUtil
PAGE_IMAGES_DIR = 'pdfPages'
PAGE_BLOCKS_DIR = 'pageBlocks'


def preProcess(img):

# batch, name, page = sys.argv[1:]
# pageFile = "{}/{}-{}-page-{}.jpg".format(PAGE_IMAGES_DIR, batch, name, page)
# img = cv2.imread(pageFile)

	filtered = ImgUtil.applyFilter(img)
	blockified = ImgUtil.blockify(filtered)
	return blockified



# outFile = "{}/{}-{}-page-{}-PAGE_BLOCKS_DIR.jpg".format(PAGE_BLOCKS_DIR, batch, name, page)
# ImgUtil.display(toSave)

# cv2.imsave(toSave, outFile)

# ImgUtil.display(filtered)
