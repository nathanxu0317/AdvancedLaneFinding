# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 20:13:25 2019

@author: xfigh
"""

import cv2
import numpy as np


def hls_lthresh(img, thresh=(100, 255)):
    # 1) Convert to HLS color space
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    hls_l = hls[:,:,1]
    hls_l = hls_l*(255/np.max(hls_l))
    # 2) Apply a threshold to the L channel
    binary_output = np.zeros_like(hls_l)
    binary_output[(hls_l > thresh[0]) & (hls_l <= thresh[1])] = 1
    # 3) Return a binary image of threshold result
    return binary_output

def hls_sthresh(img, thresh=(100, 255)):
    # 1) Convert to HLS color space
    hls = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
    hls_l = hls[:,:,2]
    hls_l = hls_l*(255/np.max(hls_l))
    # 2) Apply a threshold to the L channel
    binary_output = np.zeros_like(hls_l)
    binary_output[(hls_l > thresh[0]) & (hls_l <= thresh[1])] = 1
    # 3) Return a binary image of threshold result
    return binary_output


def rgb_rthresh(img, thresh=(220, 255)):
    r = img[:,:,0]
    r = r*(255/np.max(r))
    # 2) Apply a threshold to the L channel
    binary_output = np.zeros_like(r)
    binary_output[(r > thresh[0]) & (r <= thresh[1])] = 1
    # 3) Return a binary image of threshold result
    return binary_output