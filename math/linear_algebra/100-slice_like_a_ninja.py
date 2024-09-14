#!/usr/bin/env python3
"""
Slice arrays along specific axes
"""


def np_slice(matrix, axes=None):
    """Slices a matrix

    Args:
        matrix (list of lists): matrix to slice
        axes (dict): dictionary where the key is an axis to slice along

    Returns:
        list of lists: the sliced matrix
    """
    if axes is None:
        return matrix

    s = []
    n = len(matrix.shape) if hasattr(matrix, 'shape') else len(matrix)

    for i in range(n):
        if i in axes:
            s.append(slice(*axes[i]))
        else:
            s.append(slice(None))

    return matrix[tuple(s)]
