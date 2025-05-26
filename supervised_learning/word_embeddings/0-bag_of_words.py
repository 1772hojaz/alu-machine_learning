#!/usr/bin/env python3

"""
Function called bags_of_words(sentences, vocab=None)
"""

from sklearn.feather_extraction.text import CountVectorizer

def bag_of_words(sentences, vocab=None):
    """
        this function creates a bag of words embedding matrix
    """
    vectorizer = CountVectorizer(vocabulary=vocab)
    X_train_counts = vectorizer.fit_transform(sentences)
    embeddings = X_train_counts.toarray()
    features = vectorizer.get_feature_names()
    return embeddings, features
