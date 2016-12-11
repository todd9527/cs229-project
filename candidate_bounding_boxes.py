# candidate_bounding_boxes.py 
# Input: a list of filenames (of images with redacted text)
# Output: a list of new files that contain the bounding boxes corresponding to each input image 
# (output of form )
import cv2
import sys 
import csv
import numpy as np
from sklearn import metrics
from matplotlib import pyplot as plt


#NONWHITE_THRESHOLD = 0.4 # Percentage of pixels that must be black for the  
MAX_CLUSTERS = 12 # Maximum number of possible clusters per image 
SELECTED_CLUSTERS = 3 # Must be <= MAX_CLUSTERS 
OUTPUT_FILENAME = 'candidate_boxes_' # Do not include csv extension 

# # Input: numpy image matrix 
# # Output: list of coordinates that correspond to low-resolution pixels
# # of the input image that contain text 
# def generate_points(img): 

# 	# Make image low resolution

# 	# Choose pixels above the threshold for clustering 


# Note: This description is from: http://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html#sklearn.metrics.silhouette_score
# The Silhouette Coefficient is calculated using the mean intra-cluster distance (a)
# and the mean nearest-cluster distance (b) for each sample. The Silhouette Coefficient 
# for a sample is (b - a) / max(a, b). To clarify, b is the distance between a sample and
# the nearest cluster that the sample is not a part of. Note that Silhouette Coefficent 
# is only defined if number of labels is 2 <= n_labels <= n_samples - 1.
# def silhouette_coefficient(points, clusters, assignments):
# 	# mean_ic_dist = 0 # Mean intra-cluster distance
# 	# mean_nc_dist = 0 # Mean nearest-cluster distance 
# # 	> X = dataset.data
# # >>> y = dataset.target
# # In normal usage, the Silhouette Coefficient is applied to the results of a cluster analysis.
# # >>>
# # >>> import numpy as np
# # >>> 





# Returns list of random clusters within the given shape
# def init_clusters(num_clusters, shape): 


# img(x:x+w, y:y+h) = 255


# **********************
# IMPORTANT TODO: if clusters are very close together, return k-means  
# with only 1 cluster (for now we are assuming >= 2 clusters per page)
#***********************


# bounding_box_list = preprocessor.find_text(image)

def get_bounding_boxes(points, labels, num_clusters):
	bounding_boxes = []
	for cluster_count in range(0, num_clusters):
		filtered_points = points[ points[:, :] == cluster_count ]
		bounding_boxes.append((np.min(filtered_points[:, 1]), np.max(filtered_points[:, 1]) \
			, np.min(filtered_points[:, 2]), np.max(filtered_points[:, 2])))
	return np.array(bounding_boxes)

for i in range(1, len(sys.argv)):
	# img = cv2.imread(sys.argv[i], cv2.IMREAD_GRAYSCALE)
	# m, n = img.shape
	character_locations = [] # Character locations (derived from character bounding boxes) in corresponding pdf 
	print sys.argv[i]
	with open(sys.argv[i], 'rb') as ifile:
		readerx = csv.reader(ifile)
		for row in readerx:
			x, y, width, height = row
			character_locations.append( ((2 * float(x) + float(width)) / 2, (2 * float(y) + float(height)) / 2) )

	# best_clusters = []

	with open(OUTPUT_FILENAME + str(i) + '.csv', 'w') as ofile:
		writer = csv.writer(ofile)
		
		assignments = np.zeros((MAX_CLUSTERS + 1, len(character_locations)))
		silhouette_scores = np.zeros((MAX_CLUSTERS + 1, 1)) # Best value is 1, worst value is -1 


		# Run k-means for variable number of clusters 
		convergence_reqs = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS , 30, 1)
		points = np.array(character_locations)
		for num_clusters in range(1, MAX_CLUSTERS + 1):

			_ , assignments[num_clusters, :], centroids = cv2.kmeans(points, num_clusters, \
			 		convergence_reqs, 30, cv2.KMEANS_RANDOM_CENTERS) 
			if num_clusters > 1:
				silhouette_scores[num_clusters] = metrics.silhouette_score(points, assignments[num_clusters, :], metric='euclidean')
			else: 
				silhouette_scores[num_clusters] = 1

			indexes = np.argsort(silhouette_scores)
			indexes = indexes[::-1]
			for i in range(SELECTED_CLUSTERS):
				cluster_index = indexes[i]
				bounding_boxes = get_bounding_boxes(points, assignments[cluster_index, :])
				for bounding_box in bounding_boxes:
					xmin, xmax, ymin, ymax = bounding_box
					writer.writerow(xmin, xmax, ymin, ymax)











