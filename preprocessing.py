# -*- coding: utf-8 -*-
"""preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1slEn7ZrlyvkyOiRdeRok9T6ybVc1zhuX
"""

import torch
import numpy as np
import cv2 as cv
import subsampling

def prepare_input(iteration, tensor):
  if iteration == 1:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.Laplacian((img*255).astype(np.uint8))
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor

  if iteration == 2:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.wfilter((img*255).astype(np.uint8))
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor

  if iteration == 3:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.hfilter((img*255).astype(np.uint8))
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor


  if iteration == 4:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.vfilter((img*255).astype(np.uint8))
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor
  
  if iteration == 5:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.hfilter((img*255).astype(np.uint8),ker=1)
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor

  if iteration == 6:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.wfilter((img*255).astype(np.uint8),ker=1)
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor

  if iteration == 7:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.vfilter((img*255).astype(np.uint8),ker=1)
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor

  if iteration == 8:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.Laplacian((img*255).astype(np.uint8),ker=5)
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor

  if iteration == 9:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.Laplacian((img*255).astype(np.uint8),ker=1)
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor

  if iteration == 0:
    img = tensor.numpy().transpose(1,2,0)
    img = subsampling.Gaussian_downscale((img*255).astype(np.uint8))
    tensor = torch.from_numpy(img.transpose((2,0,1))).type(torch.float16)
    return tensor

def prepare_batch(input, n, batch_size):
  for i in range(batch_size):
    img_t = input[i,:,:,:]
    img_t = prepare_input(n,img_t)
    img_t = img_t.view(-1,3,48,72)
    if i==0:
      op = img_t
    else:
      op = torch.cat((op,img_t),dim=0)

  return op