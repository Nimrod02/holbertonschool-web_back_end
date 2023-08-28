#!/usr/bin/env python3
"""module 5 - sum_list
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """a type-annotated function sum_list
    which takes a list input_list of floats
    as argument and returns their sum as a float.

    Args:
        input_list (List[float]): list of float

    Returns:
        float: sum of the list
    """
    return sum(input_list)
