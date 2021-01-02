# https://stackoverflow.com/questions/51205502/convert-a-black-and-white-image-to-array-of-numbers

import numpy as np
import cv2
import matplotlib.pyplot as plt

my_img = cv2.imread('img/HUGS.bmp')
inverted_img = (255.0 - my_img)
final = inverted_img / 255.0

# Visualize the result
plt.imshow(final)
plt.show()

print(final.shape)
print(type(final))
print(final)
print(final[:,7])