# -*- coding: utf-8 -*-
"""
Created on Sat Apr 14 00:24:57 2018

@author: user
"""

import numpy as np
import pylab as pl
from skimage.io import imread
from skimage.color import rgb2gray, rgb2hsv
from scipy import ndimage as ndi
import time
import voronoi

imrgb = imread('p1.jpg'); pl.figure(); pl.imshow(imrgb)

imhsv = rgb2hsv(imrgb)
hcomp = imrgb[:,:,0]
binary = (50 < hcomp) & (hcomp < 165)
im_filled = ndi.binary_fill_holes(binary).astype(np.uint8)

#im_filled = im_filled  * 255


start_time = time.time()
im_filled = voronoi.thin(im_filled, "guo_hall_fast")
print("--- %s seconds ---" % (time.time() - start_time))

pl.figure(); pl.imshow(im_filled)

pl.show()






