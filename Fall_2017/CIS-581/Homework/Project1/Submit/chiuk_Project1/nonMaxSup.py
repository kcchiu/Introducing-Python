'''
  File name: nonMaxSup.py
  Author:
  Date created:
'''

'''
  File clarification:
    Find local maximum edge pixel using NMS along the line of the gradient
    - Input Mag: H x W matrix represents the magnitude of derivatives
    - Input Ori: H x W matrix represents the orientation of derivatives
    - Output M: H x W binary matrix represents the edge map after non-maximum suppression
'''
#from interp import interp2
import numpy as np
import scipy

def nonMaxSup(Mag, Ori):
    M = np.zeros(Mag.shape)
    #x_mesh, y_mesh = np.meshgrid(np.arange(Mag.shape[1]),np.arange(Mag.shape[0]))
    #magcos = Mag*np.cos(Ori)
    #magsin = Mag*np.sin(Ori)
    #xq_mesh, yq_mesh = np.meshgrid(magcos,magsin)
    
    for i in xrange(1,Mag.shape[0]-1,1):
        for j in xrange(1,Mag.shape[1]-1,1):
            
            m_new_up = i-np.sin(Ori[i][j])
            n_new_up = j+np.cos(Ori[i][j])
            m_new_dn = i+np.sin(Ori[i][j])
            n_new_dn = j-np.cos(Ori[i][j])
            
#            m_new_up = i+np.sin(Ori[i][j])
#            n_new_up = j-np.cos(Ori[i][j])
#            m_new_dn = i-np.sin(Ori[i][j])
#            n_new_dn = j+np.cos(Ori[i][j])
            #print "a", j

            a = np.array([i,i-1,i-1,i])
            b = np.array([j,j,j+1,j+1])
            c = np.array([i,i+1,i+1,i])
            d = np.array([j,j,j-1,j-1])
            
            v_up=np.array([Mag[i,j],Mag[i-1,j],Mag[i-1,j+1],Mag[i,j+1]])
            v_dn=np.array([Mag[i,j],Mag[i+1,j],Mag[i+1,j-1],Mag[i,j-1]])

            Mag_up = scipy.interpolate.interp2d(a,b,v_up)
            Mag_dn = scipy.interpolate.interp2d(c,d,v_dn)
            
            Mag_up_ij = Mag_up(m_new_up, n_new_up)
            Mag_dn_ij = Mag_dn(m_new_dn, n_new_dn)

            if Mag[i][j] > Mag_up_ij and Mag[i][j] > Mag_dn_ij:
                M[i][j] = 1
            else:
                M[i][j] = 0
            

    #np.savetxt('/M_result',Mag)
    return M
  # TODO: your code here