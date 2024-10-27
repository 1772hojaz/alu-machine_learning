#!/usr/bin/env python3
"""
Performs pooling on images.
"""
import numpy as np


def pool(images, kernel_shape, stride, mode='max'):
    """
    Performs pooling on images.

    Args:
        images: A numpy.ndarray of shape (m, h, w, c)
        containing multiple images.
        kernel_shape: A tuple (kh, kw) containing the
        kernel shape for pooling.
        stride: A tuple (sh, sw) specifying the
        stride for height and width.
        mode: A string ('max' or 'avg') indicating the pooling mode.

    Returns:
        A numpy.ndarray containing the pooled images.
    """
    m, height, width, c = images.shape
    kh, kw = kernel_shape
    sh, sw = stride

    ph = ((height - kh) // sh) + 1
    pw = ((width - kw) // sw) + 1
    pooled = np.zeros((m, ph, pw, c))

    for i, h in enumerate(range(0, (height - kh + 1), sh)):
        for j, w in enumerate(range(0, (width - kw + 1), sw)):
            if mode == 'max':
                output = np.max(images[:, h:h + kh, w:w + kw, :], axis=(1, 2))
            elif mode == 'avg':
                output = np.average(images[:, h:h + kh, w:w + kw, :],
                                    axis=(1, 2))
            else:
                pass
            pooled[:, i, j, :] = output

    return pooled
