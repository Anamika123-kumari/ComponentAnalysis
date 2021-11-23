# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:13:16 2021

@author: anam2
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.decomposition import NMF
from sklearn.decomposition import DictionaryLearning

def show_orignal_images(image):
	#Displaying images
	fig, axes = plt.subplots(6, 10, figsize=(11, 7),
	                         subplot_kw={'xticks':[], 'yticks':[]})
	for i, ax in enumerate(axes.flat):
        
	    ax.imshow(np.array(image)[i].reshape(4, 4),cmap='gray')
        
	plt.show()   

df=pd.read_csv("img_pixels3.csv")
my_array=df.to_numpy()
my_arrayt=np.transpose(my_array)
print(my_array.shape) 
show_orignal_images(my_array) 
pca=PCA(n_components=5)
pca.fit(my_array)
pca_comp=(pca.components_)
print("shape of pca  component."+str(pca_comp.shape))
fig, axes = plt.subplots(1,5, figsize=(9, 4),
	                         subplot_kw={'xticks':[], 'yticks':[]})
for i, ax in enumerate(axes.flat):
	    ax.imshow(pca_comp[i].reshape(4, 4), cmap='gray')
	    ax.set_title("PC " + str(i+1))
plt.show() 
#nmf  
nmf=NMF(n_components=5,max_iter=1000)
nmf.fit(my_array)
nmf_comp=(nmf.components_)
print("shape of nmf component."+str(nmf_comp.shape))
fig, axes = plt.subplots(1,5, figsize=(9, 4),
	                         subplot_kw={'xticks':[], 'yticks':[]})
for i, ax in enumerate(axes.flat):
	    ax.imshow(nmf_comp[i].reshape(4, 4), cmap='gray')
	    ax.set_title("PC " + str(i+1))
        
plt.show()
'''dl=DictionaryLearning(n_components=5,max_iter=1000)
dl.fit(my_array)
dl_comp=(dl.components_)
dl_comp'''









