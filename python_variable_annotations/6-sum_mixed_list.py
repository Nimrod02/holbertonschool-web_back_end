#!/usr/bin/env python3
"""module 6 - sum_mixed_list
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ a type-annotated function sum_mixed_list
    which takes a list mxd_lst of integers and floats
    and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): list with int and float

    Returns:
        float: return the sum of the list
    """
    return sum(mxd_lst)
