
# coding: utf-8

# # CIS-581 Homework 1

# In[1]:

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from PIL import Image


# In[2]:

# -- Read an image --
# Attribution - Bikesgray.jpg By Davidwkennedy (http://en.wikipedia.org/wiki/File:Bikesgray.jpg) [CC BY-SA 3.0 (http://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons
img1 =  Image.open("Bikesgray.jpg")# Write code here to read in the image named 'Bikesgray.jpg' into the variable img1

# -- Display original image --
img1.show()


# In[3]:

# -- X gradient - Sobel Operator --
f1 = np.asarray([[1, 0, -1], [2, 0, -2], [1, 0, -1]])

# -- Convolve image with kernel f1 -> This highlights the vertical edges in the image --
vertical_sobel =  signal.convolve2d(img1,f1)# Write code here to convolve img1 with f1


# In[4]:

# -- Display the image --
# Write code here to display the image 'vertical_sobel' (hint: use plt.imshow with a color may of gray)
plt.imshow(vertical_sobel,cmap='gray')
plt.show()


# In[5]:

# -- Y gradient - Sobel Operator --
f2 = np.asarray([[ 1, 2, 1], [0, 0, 0], [-1, -2, -1]])
# Now if you want to highlight horizontal edges in the image, think about what the kernel should be. Store this kernel in the variable f2.


# In[6]:

# -- Convolve image with kernel f2 -> This should highlight the horizontal edges in the image --
horz_sobel = signal.convolve2d(img1,f2)# Write code here to convolve img1 with f2

# -- Display the image --
# Write code here to display the image 'horz_sobel' (hint: use plt.imshow with a color may of gray)
plt.imshow(horz_sobel,cmap='gray')
plt.show()


# In[ ]:



