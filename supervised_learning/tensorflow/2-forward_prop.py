#!/usr/bin/env python3
'''
    Forward propagation
'''


import tensorflow as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes, activations):
    '''
        args:
        x : is the placeholder for the input data
        layer_sizes : is a list containing the
            number of nodes in each layer of the network
        activations : is a list containing the activation
            functions for each layer of the network
    '''
    output = x
    for size, activation in zip(layer_sizes, activations):
        output = create_layer(output, size, activation)
    return output
