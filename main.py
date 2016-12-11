# main.py
import os
import util
import BoundCharacters as bc
import re
from sklearn.cluster import KMeans
import math
import csv

RAW_PDF_DIR = 'rawPDFs'
PDF_PAGES_DIR = 'pdfPages'


# Take in list of pdf URLs - save to local folder
pdfURLs = util.csvToList("pdfURLs.csv")
pdfs = [{'name': 'pdf{}'.format(ind), 'url': x['url'], 'path': "{}/pdf{}".format(RAW_PDF_DIR,ind)} for ind, x in enumerate(pdfURLs)]

for pdf in pdfs:
	name = pdf['name']
	# util.getPdfFromURL(pdf['url'], pdf['path']) #You can comment this out to save time
	# util.splitPDF(name, RAW_PDF_DIR, PDF_PAGES_DIR)  #You can comment this out to save time
	pages = [{'filename':filename, 'pgNum': int(re.split("\.|\-", filename)[1])} for filename in os.listdir('./{}'.format(PDF_PAGES_DIR)) if filename.startswith(name)]
	pages.sort(key = lambda x: x['pgNum'])

	for page in pages:

		"""see note 1"""

		characterBoxes = bc.getCharacterBoundingBoxes('{}/{}'.format(PDF_PAGES_DIR,page['filename']))


		# Save character bounding boxes here
		print characterBoxes

		with open("characterBoxes/{}-pg{}-charboxes.csv".format(page['filename'], page['pgNum']), "wb") as f:
		    writer = csv.writer(f)
		    writer.writerows(characterBoxes)



		# characterPoints = list(map(lambda p: util.getBoxCenterPoint(p[0],p[1],p[2],p[3]), characterBoxes))



		# Add an if statement s.t. if there are no points to cluster it doesn't attempt this
		# if len(characterPoints) > 100:
		# 	kmeans = KMeans(n_clusters=10, random_state=0).fit(characterPoints)
		# 	# labelled = kmeans.fit_predict()
		# 	centroids = [(int(math.floor(x[0])), int(math.floor(x[1]))) for x in kmeans.cluster_centers_]

		# 	# for each centroid assign your points
		# 	# labelled = kmeans.


		# 	print centroids

		# 	util.showImage('{}/{}'.format(PDF_PAGES_DIR,page['filename']), color=None, boundingBoxes=None, bbColor=None)
		# 	util.showImage('{}/{}'.format(PDF_PAGES_DIR,page['filename']), color=None, boundingBoxes=characterBoxes, bbColor=None)
		# 	util.showImage('{}/{}'.format(PDF_PAGES_DIR,page['filename']), color=None, points=characterPoints, bbColor=None)
		# 	util.showImage('{}/{}'.format(PDF_PAGES_DIR,page['filename']), color=None, points=centroids, bbColor=None)



# >>> import numpy as np
# >>> X = np.array([[1, 2], [1, 4], [1, 0],
# ...               [4, 2], [4, 4], [4, 0]])
# >>> kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
# >>> kmeans.labels_
# array([0, 0, 0, 1, 1, 1], dtype=int32)
# >>> kmeans.predict([[0, 0], [4, 4]])
# array([0, 1], dtype=int32)
# >>> kmeans.cluster_centers_
# array([[ 1.,  2.],
#        [ 4.,  2.]])

		# for i in xrange(len(characterBoxes)):
		# 	print characterBoxes[i]
		# 	print characterPoints[i]

		# getBoxCenterPoint(x,y,w,h)]

		# items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))

		"""See note 2"""

		# get the center point from each bounding box
		# apply k means


		

		





"""
note 1: you may want to add some transformations to the page image here
"""

	

"""
note 2: I could/should add a save point here - save coordinates of bounding boxes to a csv with a name related to the page
		# with open('filename', 'wb') as myfile:
	 #   		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		#     wr.writerow(mylist)

		# 	characterBoxFile = open(..., 'wb')
		# 	charBoxFilename = 'charboxes/{}'.format(page['filename'])
		# 	wr = csv.writer(characterBoxFile, quoting=csv.QUOTE_ALL)
		# 	wr.writerow(characterBoxes)

"""


# To show the bounding boxes for characters on a sample image
# bbs = bc.getCharacterBoundingBoxes("myDir/testing-23.jpg")
# util.showBoundingBoxes("myDir/testing-23.jpg", bbs)