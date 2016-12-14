#Input params: <batch> <name> <num_pages>

import sys 
import model
import model_util 

def main():
	if len(sys.argv) != 4:
		return
	batch = sys.argv[1]
	name = sys.argv[2]
	num_pages = int(sys.argv[3])
	#cropped_images, labels = model_util.prepare_data(batch, name, num_pages)
	#print cropped_images[0], labels[0]
	#print len(cropped_images), len(labels)
	# cnn_model = model.CNN_Model()
	# cnn_model.train_model(cropped_images, labels)

	cnn_model = model.CNN_Model()
	cnn_model.train_model([], [])




if __name__ == "__main__":
    main()
