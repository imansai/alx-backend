#!/usr/bin/env python3
"""Pagination simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Takes in the index range from specified pages sizes.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
