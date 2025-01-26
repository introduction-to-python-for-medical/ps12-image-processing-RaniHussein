from image_utils import load_image, edge_detection
from PIL import Image
import numpy as np
from skimage.filters import median
from skimage.morphology import ball
path = 'starry night.jpg'
picture = load_image(path)
clean_image = median(picture, ball(3))
thefinal = edge_detection(clean_image)
binary_image = thefinal < 100

binary = Image.fromarray(binary_image)
binary.save('mybinary.png')
