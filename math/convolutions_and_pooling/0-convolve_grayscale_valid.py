#!/usr/bin/env python3
"""
    a function convolve_valid that performs a valid convolution on
    grey scale images.
"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    Performs a valid convolution on grayscale images.

    Args:
        images:  
        A numpy.ndarray of shape (m, h, w)
        containing multiple grayscale images.
        kernel: A numpy.ndarray of shape (kh, kw) containing the
        kernel for the convolution.

    Returns:
        A numpy.ndarray containing the convolved images.
    """
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
