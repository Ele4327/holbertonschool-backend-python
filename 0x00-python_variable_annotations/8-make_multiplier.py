#!/usr/bin/env python3

from typing import Callable
# A type-annotated function that takes a float (multiplier) and returns
# a function that multiplies another float by the previous one(multiplier).


def make_multiplier(multiplier: float) -> Callable[[float], float]:

    def other_function(n: float) -> float:
        return n * multiplier

    return other_function
