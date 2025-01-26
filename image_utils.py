from PIL import Image
import numpy as np
from scipy.signal import convolve2d
path = 'starry night.jpg'
def load_image(path):
  image = Image.open(path)
  image = np.array(image)
  return image

def edge_detection(image):
  grey_night = np.mean(image, axis = 2)
  kernelY = np.array([[1 , 2 , 1],[0 , 0 , 0],[-1 , -2 , -1]])
  kernelX = np.array([[-1 , 0 , 1],[-2 , 0 , 2],[-1 , 0 , 1]])
  edgeX = convolve2d(grey_night ,kernelX)
  edgeY = convolve2d(grey_night ,kernelY)
  edgeMAG = ((edgeX **2) + (edgeY **2)) **0.5
  return edgeMAG
