#!/usr/bin/env python3

"""
Function called bags_of_words(sentences, vocab=None)
"""

from sklearn.feather_extraction.text import CountVectorizer

def bag_of_words(sentences, vocab=None):
    """
        this function creates a bag of words embedding matrix
    """
    bow = CountVectorizer(vocabulary=vocab)
    matrix = bow.fit_transform(sentences).toarray()
    features = List(bow.vocabulary_.keys()) if vocab else bow.get_feature_names_out().toList()
    return matrix, features
