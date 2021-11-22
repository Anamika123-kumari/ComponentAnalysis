# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:54:38 2021

@author: anam2
"""

from PIL import Image
import numpy as np
#import sys
import os
import csv
def createFileList(myDir, format='.png'):
    fileList = []
    #print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList
header=[]
for i in range(0,16):
    header.append(i)

with open("img_pixels3.csv", 'w',newline='') as file:
    dw = csv.DictWriter(file, delimiter=',', 
                        fieldnames=header)
    dw.writeheader()
myFileList = createFileList('C:/Users/anam2/Desktop/data_sets')  
for file in myFileList:
    
    img_file = Image.open(file)
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode
    img_grey = img_file.convert('L')
    value = np.asarray(img_grey.getdata(), dtype=np.int64).reshape((img_grey.size[1], img_grey.size[0]))
    value = value.flatten()
    with open("img_pixels3.csv", 'a', newline='') as f:
        
        writer = csv.writer(f)
        writer.writerow(value)
