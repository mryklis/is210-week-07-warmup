#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module evaluates truthiness."""


def bool_to_str(bval):
    """Function compares boolean values and returns string

    Args:
        bval (bool): either has text or empty

    Returns:
        strval (str): returns 'Yes' or 'No'

    Example:
        >>> import task_02
        >>> bool_to_str(True)
        'Yes'

        >>> import task_02
        >>> bool_to_str('')
        'No'
        """
    if bval:
        strval = 'Yes'
    else:
        strval = 'No'
    return strval
