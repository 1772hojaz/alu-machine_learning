#!/usr/bin/env python3
'''
    Train the model
'''

import tensorflow as tf


def create_train_op(loss, alpha):
    '''
        args:
        loss : is the loss of the network’s prediction
        alpha : is the learning rate
        Returns: an operation that trains the network using gradient descent
    '''
    return tf.train.GradientDescentOptimizer(alpha).minimize(loss)
