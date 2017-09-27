'''
  File name: edgeLink.py
  Author:
  Date created:
'''

'''
  File clarification:
    Use hysteresis to link edges based on high and low magnitude thresholds
    - Input M: H x W logical map after non-max suppression
    - Input Mag: H x W matrix represents the magnitude of gradient
    - Input Ori: H x W matrix represents the orientation of gradient
    - Output E: H x W binary matrix represents the final canny edge detection map
'''

import numpy as np

def edgeLink(M, Mag, Ori):
#    threshold_high = 0.17
#    threshold_low = 0.05
#    high = threshold_high * Mag.max
#    low = threshold_low * Mag.min
#    
#    p_Mag = np.multiply(M,Mag)
#    
##    for i in xrange(Mag.shape[0]):
##        for j in xrange(Mag.shape[1]):
##            if p_Mag[i]
    M = M*Mag
    threshold_low = 0.1 #0.05
    threshold_high = 0.9 #0.5
    low = threshold_low * np.amax(M)
    high = threshold_high * np.amax(M)
    
    edges = np.zeros(Mag.shape)
    
    for i in xrange(1,Mag.shape[0]-1,1):
        for j in xrange(1,Mag.shape[1]-1,1):
            if Mag[i][j] > low and Mag[i][j] < high:
                edges[i][j] = 1
            else:
                edges[i][j] = 0
            
            
    
    return edges
  # TODO: your code here