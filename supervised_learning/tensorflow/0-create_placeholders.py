#!/usr/bin/env python3
'''
    function create_placeholders(nx, classes):
'''

import tensorflow as tf


def create_placeholders(nx, classes):
    '''
        args:
        nx: the number of feature columns in our data
        classes: the number of classes in our classifier

    '''
    x = tf.placeholder(tf.float32, shape=(None, nx), name='x')
    y = tf.placeholder(tf.float32, shape=(None, classes), name='y')
    return x, y
