#*****USAGE*******
# python train_model.py <label prefix> <image prefix> <num train pages> 
# python train_model.py label- image- 50
# output: model.tfl 

from __future__ import division, print_function, absolute_import

import tflearn
from tflearn.data_utils import shuffle
from tflearn.layers.core import input_data, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.estimator import regression
from tflearn.data_augmentation import ImageAugmentation
import scipy
import numpy as np 

# Constants for scripting (IO, ect)
MODEL_FILENAME = 'model.tfl'

# Constants for CNN 
IMG_WIDTH = 60         # Scale all train images to these dimensions of pixels 
IMG_HEIGHT = 40
CHANNELS = 1           # Number of color channels (eg, 3 for RGB)
CONV_FILTERS = 32
CONV_FILTER_SIZE = 2
DOWNSAMPLE_SIZE = 2    # Side length of downsampling square 

def resize_images(image_list): 
	return [resize_image(image) for image in image_list]

def resize_image(image):
	return scipy.misc.imresize(image, (IMG_HEIGHT, IMG_WIDTH)).astype(np.float32)

def init_cnn_model(): 
	# Rotate input images 
	img_aug = ImageAugmentation()
	img_aug.add_random_flip_leftright()
	input_tensor = input_data(shape=[None, IMG_HEIGHT, IMG_WIDTH, CHANNELS], data_augmentation=img_aug)

	# Create CNN 
	network = conv_2d(input_tensor, CONV_FILTERS, CONV_FILTER_SIZE)
	network = max_pool_2d(network, DOWNSAMPLE_SIZE)
	network = conv_2d(network, CONV_FILTERS * 2, CONV_FILTER_SIZE)
	network = max_pool_2d(network, DOWNSAMPLE_SIZE)
	network = fully_connected(network, 512)
	network = fully_connected(network, 2, activation='softmax')
	network = regression(network, loss='mean_square', learning_rate=0.001)

	# Write model to file 
	model = tflearn.DNN(network)

	return model 

class CNN_Model():

	def __init__(self):
		self.model = init_cnn_model()

												    # (or have this taken care of in script that compiles together all of the images)
	def train_model(self, cropped_train_images, labels):  # NOTE: perhaps contain label filenames, bounding box filenames, and image filenames
		# Train using CNN 
		self.model = init_cnn_model()
		self.model.fit(resize_images(cropped_train_images), labels, n_epoch=100, shuffle=True)
		self.model.save(MODEL_FILENAME)

	def test_model(self, cropped_test_images, labels):
		cropped_test_images = resize_images(cropped_test_images)
		self.model = init_cnn_model()
		self.model.load(MODEL_FILENAME)
	    preds = [ self.model.predict(image) for image in cropped_test_images]
	    correct = [labels[i] = preds[i] for i in range(len(preds))]
	    correct_true = [labels[i] == 1 and preds[i] == 1 for i in range(len(preds))]
	    print "------Table Locator CNN--------"
	    print "Accuracy = %f", len(correct) / len(preds)
	    print "Recall = %f", len(correct_true) / sum(labels)
	    #TODO: add precision





