#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module produces the max, min, and avg words per line."""


import decimal

def lexicographics(to_analyze):
     """Function produces fibonacci sequence up to the maxint

     Args:
          to_analyze (str): input string to be analyzed
    
     Returns:
         tup (tuple): tuple containing 2 integers and a decimal.
    
    Example:
        >>> lexicographics('''Don't stop believing,
        Hold on to that feeling.''')
        (5, 3, Decimal(4.0))
    """

    count_words = []
    for char in to_analyze.split('\n'):
        length = len(char.split(' '))
        count_words.append(length)
    avg = decimal.Decimal(sum(count_words))/len(count_words)
    max_words = max(count_words)
    min_words = min(count_words)
    tup = max_words, min_words, avg
    return tup
