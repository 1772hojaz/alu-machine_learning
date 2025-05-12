#!/usr/bin/env python3
#a class that performs tasks for neural style transfer

class NSF:
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'
    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        style_image = style_image
        content_image = content_image
        alpha = alpha
        beta = beta

    if type(style_image) is not np.ndarry
