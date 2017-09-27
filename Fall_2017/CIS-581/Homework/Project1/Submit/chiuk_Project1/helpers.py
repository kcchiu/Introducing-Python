'''
  File name: helpers.py
  Author: Kuan-Cheng Chiu
  Date created: 9/27/2017
'''

'''
  File clarification:
    Helpers file that contributes the project
    You can design any helper function in this file to improve algorithm
'''

import matplotlib.pyplot as plt
import numpy as np

def challenge_3(I,im, E):
    #plt.imshow(I[:,:,0])
    pix = im.convert(mode='RGB')
    pix = im.load()
    
    temp_img = np.zeros(I.shape)
    finl_img = np.zeros(I.shape)
    
    red_img = np.zeros(I.shape)
    blu_img = np.zeros(I.shape)
    grn_img = np.zeros(I.shape)
    
    #print temp_img.shape
    
    for i in xrange(im.size[0]):
        for j in xrange(im.size[1]):
            temp_img[j][i][2] = pix[i,j][0]
            temp_img[j][i][1] = pix[i,j][1]
            temp_img[j][i][0] = pix[i,j][2]
                                    
    #E=E*red_img
    red_img[...,0] = E * temp_img[...,0]
    blu_img[...,1] = E * temp_img[...,1]
    grn_img[...,2] = E * temp_img[...,2]
    
    finl_img[...,0] = E * temp_img[...,0]
    finl_img[...,1] = E * temp_img[...,1]
    finl_img[...,2] = E * temp_img[...,2]
    #print red_img, blu_img, grn_img
    
    fig, axis = plt.subplots(2, 3, figsize = (20, 20))
    axis[0,0].imshow(I)
    axis[0,1].imshow(finl_img)
    axis[0,2].imshow(E, cmap='gray')
    axis[1,0].imshow(red_img)
    axis[1,1].imshow(blu_img)
    axis[1,2].imshow(grn_img)
    
    #print temp_img.shape, red_img.shape, E.shape   
    plt.show()
    
    return 0