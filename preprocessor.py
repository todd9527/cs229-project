# Goal: to quickly turn a pdf into a "purer" image


# Assume I can already pull an image
get the image
grey it
ocr it




# Steps:
	# Pull the pdfs
	# greyscale
	# OCR
	# Redact



# Step 1/ Get it from address
# import urllib
# def getRawPDF(url, name):
# 	file = urllib.URLopener()
# 	file.retrieve(url, "{}.pdf".format(name))
# 	return file

# testURL = "http://s3-us-west-2.amazonaws.com/ori-cacs/07-06/1-1-1-1_Alabama_COUNTY_AUTAUGA_CAFR_2009.pdf"

# rawPDF = getRawPDF(testURL, "test")


# testfile = urllib.URLopener()
# testfile.retrieve(url, "testfile.pdf")

# Step 2/ Grey it [skipping this step for now]

# Approach 1
# gs -sOutputFile=grayscale.pdf -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -dCompatibilityLevel=1.4 -dNOPAUSE -dBATCH testfile.pdf

# Approach 2
# from PIL import Image
# img = Image.open('testfile.png').convert('LA')
# img.save('greyscale.png')

# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg


# Approach 3
# def rgb2gray(rgb):
#     return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

# img = mpimg.imread('testfile.pdf')     
# gray = rgb2gray(img)    
# plt.imshow(gray, cmap = plt.get_cmap('gray'))
# plt.show()

#Step 3/OCR the pdfs
# I loaded this:
# brew install tesseract
# brew install ghostscript
# brew install poppler
# brew install imagemagick

#Step 4/Redact all text 

# Segment it 

