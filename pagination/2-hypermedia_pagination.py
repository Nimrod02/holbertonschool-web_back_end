#!/usr/bin/env python3
"""
module 1
"""


from typing import Tuple
import csv
import math
from typing import List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """find the correct indexes to paginate
        the dataset correctly and return the appropriate page of the dataset

        Args:
            page (int): number of pages. Defaults to 1.
            page_size (int): size of a page. Defaults to 10.

        Returns:
            List[List]: list of list
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        i_range = index_range(page, page_size)

        start_page = i_range[0]
        end_page = i_range[1]

        if end_page > len(self.dataset()):
            return []
        else:
            return self.dataset()[start_page:end_page]

    def get_hyper(self, page_size=10, page=1):
        """and returns a dictionary
        containing the following key-value pairs

        Args:
            page_size (int):length of the returned dataset page. Defaults to 10
            page (int): current page number. Defaults to 1
        """
        data = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.dataset()) / page_size)

        hyper_dict = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }

        return hyper_dict
