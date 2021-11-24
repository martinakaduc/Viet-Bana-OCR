import pytesseract
import cv2
# from skimage import io
import numpy as np
from imutils import paths

inputDir = 'input/'
outputDir = 'output/'
# imageName = list(filter(lambda file: file[-3:] == 'png', os.listdir(inputDir)))
imageName = list(paths.list_images(inputDir))

def loadImage(imgPath):
    img = cv2.imread(imgPath)
    # Convert to gray scale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img

for imgPath in imageName:
    print(imgPath)
    img = loadImage(imgPath)
    # cv2.imshow("original", img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    custom_oem_psm_config = '--psm 6'

    with open(outputDir + imgPath[imgPath.rfind('/') + 1:-3] + 'txt', 'w', encoding='utf-8') as f:
        f.write(pytesseract.image_to_string(img, lang='vie', config=custom_oem_psm_config))