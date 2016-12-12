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
	cropped_images, labels = model_util.prepare_data(batch, name, num_pages)
	cnn_model = model.CNN_Model()
	cnn_model.train(cropped_images, labels)

if __name__ == "__main__":
    main()
