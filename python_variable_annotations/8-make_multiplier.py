#!/usr/bin/env python3
"""module 8 - make_multiplier
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): first number

    Returns:
        Callable[[float], float]: list of float
    """
    def multiplier_function(x: float) -> float:
        """second function for x

        Args:
            x (float): second number

        Returns:
            float: the operation with both number
        """
        return x * multiplier
    return multiplier_function
