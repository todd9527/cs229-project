# main.py
import util
import BoundCharacters as bc


# To show the bounding boxes for characters on a sample image
bbs = bc.getCharacterBoundingBoxes("myDir/testing-23.jpg")
util.showBoundingBoxes("myDir/testing-23.jpg", bbs)