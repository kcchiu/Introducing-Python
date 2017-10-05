'''
  File name: click_correspondences.py
  Author: 
  Date created: 
'''
import matplotlib.pyplot as plt
import numpy as np
import pylab
import cpselect as cps
'''
  File clarification:
    Click correspondences between two images
    - Input im1: target image
    - Input im2: source image
    - Output im1_pts: correspondences coordiantes in the target image
    - Output im2_pts: correspondences coordiantes in the source image
'''

def click_correspondences(im1, im2):
  '''
    Tips:
      - use 'matplotlib.pyplot.subplot' to create a figure that shows the source and target image together
      - add arguments in the 'imshow' function for better image view
      - use function 'ginput' and click correspondences in two images in turn
      - please check the 'ginput' function documentation carefully
        + determine the number of correspondences by yourself which is the argument of 'ginput' function
        + when using ginput, left click represents selection, right click represents removing the last click
        + click points in two images in turn and once you finish it, the function is supposed to 
          return a NumPy array contains correspondences position in two images
  '''
  #fig, axis = plt.subplots(1, 2, figsize = (20, 20))
  #axis[0].imshow(im1)
  #axis[1].imshow(im2)
  print "please click:===================="
  #im1_pts = plt.ginput(3)
  im1_pts, im2_pts = cps.cpselect(im1, im2)
  #im2_pts = 0
  print "clicked:", im1_pts
  #plt.show()

  # TODO: Your code here
  
  return im1_pts, im2_pts
