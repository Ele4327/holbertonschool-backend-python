#!/usr/bin/env python3

"""
    A type-annotated function that takes a string (k) and an
    int/float (v) as arguments and returns a tuple.
    The second element should be annotated as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ to_kv takes a string (k) and an int or float (v) and returns a tuple
    with annotation especific for the second element."""
    return(k, (pow(v, 2)))
