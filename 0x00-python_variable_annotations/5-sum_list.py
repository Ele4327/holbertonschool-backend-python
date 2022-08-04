#!/usr/bin/env python3


""" Type-annotated function which takes a list
    of floats and returns their sum as a float. """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """ The function sum_list takes a list of floats and return a total
    in float type """
    return sum(input_list)
