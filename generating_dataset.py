# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 15:44:53 2021

@author: anam2
"""

import numpy as np
import matplotlib.pyplot as plt
#generating A and it 1000 noisy samples

imgA=np.array([[1,0,0,1],[0,1,1,0],[0,0,0,0],[0,1,1,0]])
plt.imshow(imgA,cmap='gray')
j=0
for i in range(0,250):
    noise=np.random.normal(0,0.01,imgA.shape)
    img1=imgA+noise
    name='C:/Users/anam2/Desktop/imagedata/pic'+str(j)
    plt.imsave(name+'.png',img1,cmap='gray')
    j+=1
#generating U    

imgU=np.array([[0,1,1,0],[0,1,1,0],[0,1,1,0],[1,0,0,1]])
plt.imshow(imgU,cmap='gray')
j=250
for i in range(0,250):
    noise=np.random.normal(0,0.01,imgU.shape)
    img1=imgU+noise
    name='C:/Users/anam2/Desktop/imagedata/pic'+str(j)
    plt.imsave(name+'.png',img1,cmap='gray')
    j+=1  
# generating K   

img=np.array([[0,1,0,1],[0,0,1,1],[0,1,0,1],[0,1,1,0]])
plt.imshow(img,cmap='gray')
j=500
for i in range(0,250):
    noise=np.random.normal(0,0.1,img.shape)
    img1=img+noise
    name='C:/Users/anam2/Desktop/image_data/pic'+str(j)
    plt.imsave(name+'.png',img1,cmap='gray')
    j+=1
'''# generating  C     
plt.figure()
img=np.array([[1,0,0,0],[0,1,1,1],[0,1,1,1],[1,0,0,0]])
plt.imshow(img,cmap='gray')
j=750
for i in range(0,1000):
    noise=np.random.normal(0,0.1,img.shape)
    img1=img+noise
    name='C:/Users/anam2/Desktop/image_data/pic'+str(j)
    plt.imsave(name+'.png',img1,cmap='gray')
    j+=1
# generating L    
plt.figure()
img=np.array([[0,1,1,1],[0,1,1,1],[0,1,1,1],[0,0,0,0]],cmap='gray')
plt.imshow(img,cmap='gray')
j=1000
for i in range(0,250):
    noise=np.random.normal(0,0.1,img.shape,cmap='gray')
    img1=img+noise
    name='C:/Users/anam2/Desktop/image_data/pic'+str(j)
    plt.imsave(name+'.png',img1,cmap='gray')
    j+=1'''
    
 
