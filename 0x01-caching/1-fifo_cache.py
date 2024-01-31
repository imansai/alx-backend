#!/usr/bin/env python3
"""FIFO caching.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Object that provides storage and retrieval
    of items from a dict with using FIFO.
    """
    def __init__(self):
        """Cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Item added to cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Retrieves item by key.
        """
        return self.cache_data.get(key, None)
