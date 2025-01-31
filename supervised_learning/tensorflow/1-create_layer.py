#!/usr/bin/env python3
'''
    function
    create_layer(prev, n, activation):
'''


import tensorflow as tf


def create_layer(prev, n, activation):
    '''
        args: 
        prev:  is the tensor output of the previous layer
        n: is the number of nodes in the layer to create
        activation: is the activation function that the layer should use
    '''
    init = tf.contrib.layers.variance_scaling_initializer(mode='FAN_AVG')
    layer = tf.layers.Dense(n, activation=activation, kernel_initializer=init)
    return layer(prev)
