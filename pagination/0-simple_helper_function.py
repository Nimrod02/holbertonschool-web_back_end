#!/usr/bin/env python3
"""
module 0
"""


from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """function should return a tuple
    of size two containing a start index and an end index

    Args:
        page (int): number of pages
        page_size (int): size of a page
    """
    start_page = (page - 1) * page_size

    end_page = start_page + page_size

    return (start_page, end_page)
