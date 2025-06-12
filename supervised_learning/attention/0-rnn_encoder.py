#!/usr/bin/env python3
"""
A class RNNEncoder
"""


import tensorflow as tf


class RNNEncoder(tf.keras.layers.Layer):
    """
    class RNNEncoder:
    """

    def __init__(self, vocab, embedding, units, batch):
        """
        Class constructor
        """
        if type(vocab) is not int:
            raise TypeError(
                "vocab must be int representing the size of input vocabulary"
            )
        if type(embedding) is not int:
            raise TypeError(
                "embedding must be int representing dimensionality of vector"
            )
        if type(units) is not int:
            raise TypeError(
                "units must be int representing the number of hidden units"
            )
        if type(batch) is not int:
            raise TypeError("batch must be int representing the batch size")
        super(RNNEncoder, self).__init__()
        self.batch = batch
        self.units = units
        self.embedding = tf.keras.layers.Embedding(vocab, embedding)
        self.gru = tf.keras.layers.GRU(
            self.units,
            return_sequences=True,
            return_state=True,
            recurrent_initializer="glorot_uniform",
        )

    def initialize_hidden_state(self):
        """
        Initializes the hidden states for the
        RNN cell to a tensor of zeros

        Returns:
            -  tensor of shape
        """
        hidden_states = tf.zeros(shape=(self.batch, self.units))
        return hidden_states

    def call(self, x, initial):
        """

        parameters:
            x: data
            initial: initial hidden state

        return:
            outputs
        """
        x = self.embedding(x)
        outputs, hidden = self.gru(x, initial_state=initial)
        return outputs, hidden
