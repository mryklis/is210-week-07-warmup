#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module demonstrates the fibonacci sequence."""


def fibonacci(maxint):
	"""Function produces fibonacci sequence up to the maxint
	
	Args:
	    maxint (int): number to set limit for sequence
	    
	Returns:
	    fib_list (list): returns fibonacci sequence of numbers
	    
	Example:
	    >>>fibonacci(10)
	    [0, 1, 1, 2, 3, 5, 8]
	"""
	
	a, b = 0, 1
	fib_list = [a]
	while b < maxint:
		fib_list.append(b)
		a, b = b, a+b
	return fib_list
