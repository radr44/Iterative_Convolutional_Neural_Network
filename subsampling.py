# -*- coding: utf-8 -*-
"""subsampling_non-wt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LzPdBUuJT_mF-QvbSr6sVtfdgFbwH-Pe
"""

import cv2 as cv
import numpy as np
import torch

def Gaussian_downscale(img): 
  img = cv.pyrDown(img)

  return img

def CannyEdge(img, l_bound = 20, u_bound = 200):

  img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation = cv.INTER_NEAREST )
  img = cv.Canny(img, l_bound, u_bound)
 
  return img

def hfilter(img, blur = False, ker = 3):
  ddepth = cv.CV_16S
  scale = 1
  delta = 0
  
  img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation = cv.INTER_NEAREST )
  if blur==True:
    img = cv.GaussianBlur(img, (3, 3), 0)
  grad_x = cv.Sobel(img, ddepth, 1, 0, ksize=ker, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
  abs_grad_x = cv.convertScaleAbs(grad_x)

  return abs_grad_x

def vfilter(img, blur = False, ker = 3):
  ddepth = cv.CV_16S
  scale = 1
  delta = 0
 
  img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation = cv.INTER_NEAREST )
  if blur==True:
    img = cv.GaussianBlur(img, (3, 3), 0)
  grad_y = cv.Sobel(img, ddepth, 0, 1, ksize=ker, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
  abs_grad_y = cv.convertScaleAbs(grad_y)
  return abs_grad_y

def wfilter(img, blur = False, ker = 3):
  ddepth = cv.CV_16S
  scale = 1
  delta = 0
  img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation = cv.INTER_NEAREST )
  if blur==True:
    img = cv.GaussianBlur(img, (3, 3), 0)
  grad_y = cv.Sobel(img, ddepth, 0, 1, ksize=ker, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
  abs_grad_y = cv.convertScaleAbs(grad_y)
  grad_x = cv.Sobel(img, ddepth, 1, 0, ksize=ker, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
  abs_grad_x = cv.convertScaleAbs(grad_x)
  grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
  return grad

def Laplacian(img, blur = False, ker = 3 ):
  ddepth = cv.CV_16S
  img = cv.resize(img, None, fx=0.5, fy=0.5, interpolation = cv.INTER_NEAREST )
  if blur==True:
    img = cv.GaussianBlur(img, (3, 3), 0)
  ss = cv.Laplacian(img, ddepth, ksize=ker)
  return ss