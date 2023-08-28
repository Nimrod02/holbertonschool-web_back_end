#!/usr/bin/env python3
"""module 7 - to_kv
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ a type-annotated function to_kv that takes a string k
    and an int OR float v as arguments and returns a tuple.
    The first element of the tuple is the string k.
    The second element is the square of the int/float v
    and should be annotated as a float.

    Args:
        k (str): fist variable
        v (Union[int, float]): second variable with a list of a int float

    Returns:
        Tuple[str, float]: return k and v square
    """
    return k, v ** 2
