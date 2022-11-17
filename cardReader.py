import cv2
import numpy as np
from mss import mss
from PIL import Image
import pytesseract

class Suits:
    def __init__(self):
        # Capture obj for taking screenshots and pre-processing
        cap = Capture()

        # load the input images
        img1 = cv2.imread('./Img/spades.png')
        img2 = cv2.imread('./Img/clubs.png')
        img3 = cv2.imread('./Img/hearts.png')
        img4 = cv2.imread('./Img/diamonds.png')

        # preprocess to constant size
        self.spades = cap.prelude(img1,80,80)
        self.clubs = cap.prelude(img2,80,80)
        self.hearts =cap.prelude(img3,80,80) 
        self.diamonds = cap.prelude(img4,80,80)        

    def mse(self,img1, img2):
        h, w = img1.shape
        diff = cv2.subtract(img1, img2)
        err = np.sum(diff**2)
        mse = err/(float(h*w))
        return mse
    # Ordinal (1-4) representing {Hearts, Spades, Diamonds, Clubs}
    def card_suit(self, img):
        if self.mse(self.hearts, img) <=1:
            return 1
        elif self.mse(self.spades, img) <=1:
            return 2 
        elif self.mse(self.diamonds, img) <=1:
            return 3 
        elif self.mse(self.clubs, img) <=1:
            return 4 
        else:
            return 0
class Capture:
    def click(self,x,y,w,h):
        with mss() as sct:
            #top = y, left = x 
            mon = {"top": y, "left":x, "width": w, "height":h}
            sct_img = sct.grab(mon)
            # Convert to PIL/Pillow Image
            return Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

    def prelude(self,image,x=200,y=200):
        image = self.np_trasnform(image)
        image = self.get_grayscale(image) 
        image = self.thresholding(image) 
        image = cv2.resize(image,(x,y))
        return image

    def imageToString(self,image):
        custom_config = "--psm 10"
        return pytesseract.image_to_string(image,lang='eng',config=custom_config) 

    def np_trasnform(self,image):
        return np.array(image)

        # get grayscale image
    def get_grayscale(self,image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # noise removal
    def remove_noise(self,image):
        return cv2.medianBlur(image,5)
     
        #thresholding
    def thresholding(self,image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        #dilation
    def dilate(self,image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.dilate(image, kernel, iterations = 1)
        
        #erosion
    def erode(self,image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.erode(image, kernel, iterations = 1)

        #opening - erosion followed by dilation
    def opening(self,image):
        kernel = np.ones((5,5),np.uint8)
        return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

        #canny edge detection
    def canny(self,image):
        return cv2.Canny(image, 100, 200)

        #skew correction
    def deskew(self,image):
        coords = np.column_stack(np.where(image > 0))
        angle = cv2.minAreaRect(coords)[-1]
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        return rotated




