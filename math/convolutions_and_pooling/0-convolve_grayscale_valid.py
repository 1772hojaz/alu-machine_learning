#!/usr/bin/env python3
import numpy as np

def convolve_grayscale_valid(images, kernel):
    m, n = kernel.shape
    if m == n:
        i, y, x = images.shape
        y = y - m + 1
        x = x - m + 1
        convolved_image = np.zeros((i, y, x))
        for i in range(y):
            for j in range(x):
                shadow_area = images[:, i:i + m, j:j + n]
                convolved_image[:, i, j] = \
                    np.sum(shadow_area * kernel, axis=(1, 2))
    
    return convolved_image
