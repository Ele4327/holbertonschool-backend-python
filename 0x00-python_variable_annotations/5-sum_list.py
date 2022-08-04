#!/usr/bin/env python3

from typing import List

""" Type-annotated function which takes a list
    of floats and returns their sum as a float. """


def sum_list(input_list: List[float]) -> float:
    """ sum_list takes a list of floats and return a total in float type """
    return sum(input_list)
