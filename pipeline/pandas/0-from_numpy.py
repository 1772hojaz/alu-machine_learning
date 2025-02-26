#!/usr/bin/env python3

"""
    Function that creates a pd.DataFrame from a np.ndarray
"""
import pandas as pd

def from_numpy(array):
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    df = pd.DataFrame(array, columns = columns)
    return df
