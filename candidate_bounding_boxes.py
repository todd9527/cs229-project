# candidate_bounding_boxes.py 
# Input: a list of filenames (of images with redacted text)
# Output: a list of new files that contain the bounding boxes corresponding to each input image 
# (output of form )
import cv2
import sys 
import csv
import numpy as np
from sklearn import metrics
from sklearn import cluster 
from matplotlib import pyplot as plt
import util

MAX_CLUSTERS = 12 # Maximum number of possible clusters per image    
SELECTED_CLUSTERS = 4 # Must be <= MAX_CLUSTERS 
#OUTPUT_FILENAME = 'candidate_boxes_' # Do not include csv extension 
# OUTPUT_DIR = 'BoundingBoxes'
INPUT_DIR = 'CharacterBoxes'

def reshapeLabels(labels):
	result = np.zeros((len(labels), 2))
	for i in range(len(labels)):
		result[i, :] = labels[i]
	return result

def get_bounding_boxes(points, labels, num_clusters):
	bounding_boxes = []
	#print points
	for cluster_count in range(0, num_clusters):
		labels_reshape = reshapeLabels(labels)
		filtered_points = points[ labels_reshape[:, :] == (cluster_count - 1) ]
		filtered_points = np.reshape(filtered_points, (np.shape(filtered_points)[0] / 2, 2))
		#filtered_points = points[ labels_reshape[:, \:] == (cluster_count - 1) ]
		if len(filtered_points) == 0: 
			continue
		# print np.min(filtered_points[:, 0])
		bounding_boxes.append((int(np.min(filtered_points[:, 0])), int(np.max(filtered_points[:, 0])) \
			, int(np.min(filtered_points[:, 1])), int(np.max(filtered_points[:, 1]))))
	return np.array(bounding_boxes)


# for i in range(1, len(sys.argv)):
character_locations = [] # Character locations (derived from character bounding boxes) in corresponding pdf 
if len(sys.argv) != 4:
	raise Exception('3 arguments required')

# Inputs 
batch = sys.argv[1]
pdf_number = sys.argv[2]
page_number = sys.argv[3]

with open('{}/{}-{}-page-{}-{}.csv'.format(INPUT_DIR, batch, pdf_number, page_number, INPUT_DIR), 'rb') as ifile:
	readerx = csv.reader(ifile)
	for row in readerx:
		x, y, width, height = row
		character_locations.append( ((2 * float(x) + float(width)) / 2, (2 * float(y) + float(height)) / 2) )

# if len(character_locations) == 0:
# 	continue
if len(character_locations) == 0:
	print ""
else:
	# with open(OUTPUT_FILENAME + str(i) + '.csv', 'w') as ofile:
	# 	writer = csv.writer(ofile)
		
	assignments = np.zeros((MAX_CLUSTERS + 1, len(character_locations)))
	#silhouette_scores = np.zeros((MAX_CLUSTERS + 1, 1)) # Best value is 1, worst value is -1 
	silhouette_scores = [0] * (MAX_CLUSTERS + 1)  # Best value is 1, worst value is -1 


	# Run k-means for variable number of clusters 
	convergence_reqs = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS , 30, 1)
	points = np.array(character_locations)
	onedim_points = np.array([(y) for x,y in character_locations])
	for num_clusters in range(1, MAX_CLUSTERS + 1):

		kmeans_result =  cluster.KMeans(n_clusters = num_clusters, max_iter = 30).fit(onedim_points.reshape(-1, 1))
		#kmeans_result =  cluster.KMeans(n_clusters = num_clusters, max_iter = 30).fit(points)
		assignments[num_clusters, :] = kmeans_result.labels_
		centroids = kmeans_result.cluster_centers_
		if num_clusters > 3:
			# silhouette_scores[num_clusters] = metrics.silhouette_score(points, assignments[num_clusters, :], metric='euclidean')
			silhouette_scores[num_clusters] = metrics.silhouette_score(onedim_points.reshape(-1, 1), assignments[num_clusters, :], metric='euclidean')
		else: 
			silhouette_scores[num_clusters] = 1


	indexes = np.array(silhouette_scores).argsort()[::-1]
	for j in range(SELECTED_CLUSTERS):
		cluster_index = indexes[j] 
		bounding_boxes = get_bounding_boxes(points, assignments[cluster_index, :], num_clusters)
		# *****Saved for debugging***********
		#page_num = i
		# imgfile = "{}/1-page-{}.jpg".format("pdfPages", page_num)
		#imgfile = "{}/train-1-page-{}.jpg".format("pdfPages", 65)
		#util.showImage(imgfile, color=None, boundingBoxes=bounding_boxes, points=[(int(p[0]),int(p[1])) for p in centroids], bbColor=(200,0,0))
		#************************************

		for bounding_box in bounding_boxes:
			xmin, xmax, ymin, ymax = bounding_box
			print '{} {} {} {}'.format(xmin, xmax, ymin, ymax)
			# writer.writerow([xmin, xmax, ymin, ymax])










