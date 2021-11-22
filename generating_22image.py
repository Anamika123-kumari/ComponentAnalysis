# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:19:41 2021

@author: anam2
"""
import numpy as np
import matplotlib.pyplot as plt

imgA=np.array([[0,1,1,0],[1,0,0,1],[1,1,1,1],[1,0,0,1]]) ##A
imgC=np.array([[0,1,1,1],[1,0,0,0],[1,0,0,0],[0,1,1,1]]) ##C
imgD=np.array([[1,1,1,0],[1,0,0,1],[1,0,0,1],[1,1,1,0]]) ##D
imgF=np.array([[1,1,1,1],[1,0,0,0],[1,1,1,1],[1,0,0,0]]) ##F
imgG=np.array([[0,1,1,0],[1,0,0,0],[1,0,1,1],[0,1,1,0]]) ##G
imgH=np.array([[1,0,0,1],[1,0,0,1],[1,1,1,1],[1,0,0,1]]) ##H
imgI=np.array([[0,0,1,0],[0,0,1,0],[0,0,1,0],[0,0,1,0]]) ##I
imgJ=np.array([[0,0,0,1],[0,0,0,1],[1,0,0,1],[1,1,1,1]]) ##J
imgK=np.array([[1,0,0,1],[1,0,1,0],[1,1,1,0],[1,0,0,1]]) ##K
imgL=np.array([[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,1,1,1]]) ##L
imgN=np.array([[1,0,0,1],[1,1,0,1],[1,0,1,1],[1,0,0,1]]) ##N
imgO=np.array([[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]]) ##O
imgP=np.array([[1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,0,0]]) ##P
imgQ=np.array([[1,1,1,0],[1,0,1,0],[1,1,1,0],[0,0,1,1]]) ##Q
imgR=np.array([[1,1,1,1],[1,0,0,1],[1,1,1,0],[1,0,0,1]]) ##R
imgT=np.array([[1,1,1,0],[0,1,0,0],[0,1,0,0],[0,1,0,0]]) ##T
imgS=np.array([[0,1,1,0],[0,1,0,0],[0,0,1,0],[0,1,1,0]]) ##S
imgU=np.array([[1,0,0,1],[1,0,0,1],[1,0,0,1],[0,1,1,0]]) ##U
imgV=np.array([[0,1,0,1],[0,1,0,1],[0,1,0,1],[0,0,1,0]]) ##V
imgX=np.array([[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]]) ##X
imgY=np.array([[0,1,0,1],[0,1,0,1],[0,0,1,0],[0,0,1,0]]) ##Y
imgZ=np.array([[1,1,1,0],[0,0,1,0],[0,1,0,0],[0,1,1,1]]) ##Z
#saving 1000 noisy samples  in data _sets folder
j=0
k=0
l=[imgA,imgC,imgD,imgF,imgG,imgH,imgI,imgJ,imgK,imgL,imgN,imgO,imgP,imgQ,imgR,imgT,imgS,imgU,imgV,imgX,imgY,imgZ]
while(k<len(l)):
    
    for i in range(0,1000):
        noise=np.random.normal(0,0.1,l[k].shape)
        img1=l[k]+noise
        name='C:/Users/anam2/Desktop/data_sets/pic'+str(j)
        plt.imsave(name+'.png',img1)
        j+=1 
    k=k+1