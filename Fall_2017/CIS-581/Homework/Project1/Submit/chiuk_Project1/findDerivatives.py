'''
  File name: findDerivatives.py
  Author:
  Date created:
'''

'''
  File clarification:
    Compute gradient information of the input grayscale image
    - Input I_gray: H x W matrix as image
    - Output Mag: H x W matrix represents the magnitude of derivatives
    - Output Magx: H x W matrix represents the magnitude of derivatives along x-axis
    - Output Magy: H x W matrix represents the magnitude of derivatives along y-axis
    - Output Ori: H x W matrix represents the orientation of derivatives
'''

import numpy as np
import matplotlib.pyplot as plt
import os
import utils
from scipy import signal
from PIL import Image

def findDerivatives(I_gray):
    #G_1D = utils.GaussianPDF_1D(0,0.5,10)
    G_2D = utils.GaussianPDF_2D(0,0.5,10,10)
    dx, dy = np.gradient(G_2D)
    
    Magx = signal.convolve2d(I_gray,dx,'same')
    Magy = signal.convolve2d(I_gray,dy,'same')
    Mag = np.sqrt(Magx*Magx + Magy*Magy)
    Ori = np.arctan(Magy, Magx)
    
    return Mag, Magx, Magy, Ori
