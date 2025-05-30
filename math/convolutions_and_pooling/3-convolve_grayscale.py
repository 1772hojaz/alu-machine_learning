#!/usr/bin/env python3
"""
    Performs a convolution on grayscale images
    with specified padding and stride.
"""
import numpy as np


def convolve_grayscale(images, kernel, padding="same", stride=(1, 1)):
    """
    Performs a convolution on grayscale images
    with specified padding and stride.

    Args:
        images: A numpy.ndarray of shape (m, h, w)
        containing multiple grayscale images.
        kernel: A numpy.ndarray of shape (kh, kw)
        containing the kernel for the convolution.
        padding: A string ('same' or 'valid') or a
        tuple (ph, pw) specifying the padding.
        stride: A tuple (sh, sw) specifying the
        stride for height and width.

    Returns:
        A numpy.ndarray containing the convolved images.
    """

    m = images.shape[0]
    height = images.shape[1]
    width = images.shape[2]
    kh = kernel.shape[0]
    kw = kernel.shape[1]
    sh, sw = stride
    if padding == "same":
        ph = int(((height - 1) * stride[0] + kh - height) / 2) + 1
        pw = int(((width - 1) * stride[1] + kw - width) / 2) + 1
    elif padding == "valid":
        ph = 0
        pw = 0
    else:
        ph = padding[0]
        pw = padding[1]
    images = np.pad(images, ((0, 0), (ph, ph), (pw, pw)),
                    "constant", constant_values=0)
    ch = ((height + (2 * ph) - kh) // sh) + 1
    cw = ((width + (2 * pw) - kw) // sw) + 1
    convolved_image = np.zeros((m, ch, cw))

    i = 0
    for h in range(0, (height + (2 * ph) - kh + 1), sh):
        j = 0
        for w in range(0, (width + (2 * pw) - kw + 1), sw):
            output = np.sum(images[:, h:h + kh, w:w + kw] *
                            kernel, axis=1).sum(axis=1)
            convolved_image[:, i, j] = output
            j += 1
        i += 1
    return convolved_image
