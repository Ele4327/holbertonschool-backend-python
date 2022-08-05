#!/usr/bin/env python3

""" A type-annotated function that takes a float and returns
    a function that multiplies another float by the previous one """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier take a float argument and return another function
    who multiplies another float by (multiplier)."""
    def other_function(n: float) -> float:
        return n * multiplier

    return other_function
