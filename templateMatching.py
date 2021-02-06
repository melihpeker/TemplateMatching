#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:28:57 2021

@author: melihpeker
"""
import cv2
import numpy as np
import math
from tqdm import tqdm
import sys


def rotate_bb(center_location, w, h, deg):
    theta= np.deg2rad(deg)
    center1=center_location[0];
    center2=center_location[1];
    R= np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]], np.double);
    X=([-w/2, w/2, w/2, -w/2]);
    Y=([-h/2, -h/2, h/2, h/2]);
    T = np.zeros([2,4])
    for i in range(4): 
        T[:,i,None] = np.matmul(R,np.array([[X[i]], [Y[i]]], np.double))
        
    x_lower_left=center1+T[0,0];
    x_lower_right=center1+T[0,1];
    x_upper_right=center1+T[0,2];
    x_upper_left=center1+T[0,3];
    y_lower_left=center2+T[1,0];
    y_lower_right=center2+T[1,1];
    y_upper_right=center2+T[1,2];
    y_upper_left=center2+T[1,3];
    coords = np.array([[x_lower_left, x_lower_right, x_upper_right, x_upper_left], 
                       [y_lower_left, y_lower_right, y_upper_right, y_upper_left]])

    return coords

if(len(sys.argv) < 3):
    sys.exit('Input Image or Template Image is missing.')

imgName = sys.argv[1]
templateName = sys.argv[2]

#imgName = "StarMap.png"
#templateName = "small_rot.png"

img = cv2.imread(imgName,0)
template = cv2.imread(templateName,0)
w, h = template.shape[::-1]


degrees = np.zeros([1,360])
for i in range(360) : degrees[0,i]=i
min_vals = np.zeros([360,2])
max_vals = np.zeros([360,2])
min_locs = np.zeros([360,2])
max_locs = np.zeros([360,2])
center = (w / 2, h / 2)


layerStar = img.copy() 
layerPatch = template.copy()

# using pyrDown() function 
layerStar = cv2.pyrDown(layerStar) 
layerPatch = cv2.pyrDown(layerPatch) 

ret,layerStar = cv2.threshold(layerStar,25,255,cv2.THRESH_BINARY)
ret,layerPatch = cv2.threshold(layerPatch,25,255,cv2.THRESH_BINARY)

   
# Coarse grain search    
for i in tqdm(range(0,360,2)):
    M = cv2.getRotationMatrix2D(center, degrees[0,i], 1.0)
    templateRot = cv2.warpAffine(layerPatch, M, (h, w))
 
    res = cv2.matchTemplate(layerStar,templateRot,3)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    min_vals[i] = min_val
    max_vals[i] = max_val
    min_locs[i] = min_loc
    max_locs[i] = max_loc

maxInd = np.argmax(max_vals[:,0])
top_left = max_locs[maxInd]

# Fine grain search    
for i in tqdm(range(max(maxInd-5,0),min(maxInd+5,360),1)):
#for i in tqdm(range(0,360,1)):
    M = cv2.getRotationMatrix2D(center, degrees[0,i], 1.0)
    templateRot = cv2.warpAffine(template, M, (h, w))
  
    res = cv2.matchTemplate(img,templateRot,3)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    min_vals[i] = min_val
    max_vals[i] = max_val
    min_locs[i] = min_loc
    max_locs[i] = max_loc

    
maxInd = np.argmax(max_vals[:,0])
top_left = max_locs[maxInd]

M = cv2.getRotationMatrix2D(center, degrees[0,maxInd], 1.0)
templateRot = cv2.warpAffine(template, M, (h, w))
w, h = templateRot.shape[::-1]


final_coords = rotate_bb([top_left[0]+w/2, top_left[1]+h/2], w, h, -degrees[0,maxInd])

print("\nTop Left: [" + str(int(final_coords[0,0])) + "," + str(int(final_coords[1,0]))+ "]")
print("Top Rigth: [" + str(int(final_coords[0,1])) + "," + str(int(final_coords[1,1]))+ "]")
print("Bottom Left: [" + str(int(final_coords[0,3])) + "," + str(int(final_coords[1,3])) + "]")
print("Bottom Rigth: [" + str(int(final_coords[0,2])) + "," + str(int(final_coords[1,2])) + "]")
print("Tilt Angle: " + str(degrees[0,maxInd]) + " degree")

