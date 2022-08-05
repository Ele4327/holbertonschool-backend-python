#!/usr/bin/env python3

"""
    A type-annotated function which takes a list of
    integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Takes a list of int and floats and return the total of
    that list (mxd_lst) in type float"""
    return (float(sum(mxd_lst)))
