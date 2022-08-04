#!/usr/bin/env python3

from typing import Union, Tuple

# A type-annotated function that takes a string (k) and an
# int/float (v) as arguments and returns a tuple.
# The second element should be annotated as a float.


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return(k, (pow(v, 2)))
