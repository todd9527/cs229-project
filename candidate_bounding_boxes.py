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

MAX_CLUSTERS = 3 # Maximum number of possible clusters per image 
SELECTED_CLUSTERS = 3 # Must be <= MAX_CLUSTERS 
OUTPUT_FILENAME = 'candidate_boxes_' # Do not include csv extension 

def get_bounding_boxes(points, labels, num_clusters):
	bounding_boxes = []
	for cluster_count in range(0, num_clusters):
		labels_reshape = np.repeat(np.transpose(labels[:]), 2, axis=1)
		filtered_points = points[ labels_reshape[:, :] == (cluster_count - 1) ]
		filtered_points = np.reshape(filtered_points, (np.shape(filtered_points)[0] / 2, 2))
		if len(filtered_points) == 0: 
			continue
		print np.min(filtered_points[:, 0])
		bounding_boxes.append((np.min(filtered_points[:, 0]), np.max(filtered_points[:, 0]) \
			, np.min(filtered_points[:, 1]), np.max(filtered_points[:, 1])))
	return np.array(bounding_boxes)

for i in range(1, len(sys.argv)):
	character_locations = [] # Character locations (derived from character bounding boxes) in corresponding pdf 
	print sys.argv[i]
	with open(sys.argv[i], 'rb') as ifile:
		readerx = csv.reader(ifile)
		for row in readerx:
			x, y, width, height = row
			character_locations.append( ((2 * float(x) + float(width)) / 2, (2 * float(y) + float(height)) / 2) )

	with open(OUTPUT_FILENAME + str(i) + '.csv', 'w') as ofile:
		writer = csv.writer(ofile)
		
		assignments = np.zeros((MAX_CLUSTERS + 1, len(character_locations)))
		silhouette_scores = np.zeros((MAX_CLUSTERS + 1, 1)) # Best value is 1, worst value is -1 


		# Run k-means for variable number of clusters 
		convergence_reqs = (cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS , 30, 1)
		points = np.array(character_locations)
		for num_clusters in range(1, MAX_CLUSTERS + 1):

			kmeans_result =  cluster.KMeans(n_clusters = num_clusters, max_iter = 30).fit(points)
			assignments[num_clusters, :] = kmeans_result.labels_
			print assignments[num_clusters, :]
			centroids = kmeans_result.cluster_centers_
			if num_clusters > 1:
				silhouette_scores[num_clusters] = metrics.silhouette_score(points, assignments[num_clusters, :], metric='euclidean')
			else: 
				silhouette_scores[num_clusters] = 1

			indexes = np.argsort(silhouette_scores)
			indexes = indexes[::-1]
			for i in range(SELECTED_CLUSTERS):
				cluster_index = indexes[i]
				bounding_boxes = get_bounding_boxes(points, assignments[cluster_index, :], num_clusters)
				for bounding_box in bounding_boxes:
					xmin, xmax, ymin, ymax = bounding_box
					writer.writerow([xmin, xmax, ymin, ymax])











