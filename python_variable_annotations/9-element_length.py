#!/usr/bin/env python3
"""module 9 - element_length
"""

from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """a type annoted function with list of iterable sequence

    Args:
        lst (Iterable[Sequence]): list of iterable

    Returns:
        List[Tuple[Sequence, int]]: list of tuple of sequence of int
    """
    return [(i, len(i)) for i in lst]
