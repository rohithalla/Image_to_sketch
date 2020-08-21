import numpy as np
import imageio
import scipy.ndimage
import cv2

img="img.png"

def grayscale(rgb):
	return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back):
	result=front*255/(255-back)
	result[result>255]=255
	result[back==255]=255
	return result.astype('uint8')

r=dodge(scipy.ndimage.filters.gaussian_filter(255-grayscale(imageio.imread(img)),sigma=10),grayscale(imageio.imread(img)))

cv2.imwrite('img_result.png',r)
