#!/usr/bin/env python3
"""
    A function that calculates accuracy
"""


import tensorflow as tf


def calculate_accuracy(y, y_pred):
    """
    args:
    y : is a placeholder for the labels of the input data
    y_pred : is a tensor containing the network’s predictions
    Returns: a tensor containing the decimal accuracy of the prediction
    """
    return tf.reduce_mean(
        tf.cast(tf.equal(tf.argmax(y, 1), tf.argmax(y_pred, 1)), tf.float32)
    )
