#!/usr/bin/env python3
"""Basic dictionary.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents object that provides storage and
    retrieval of items from a dictionary.
    """
    def put(self, key, item):
        """Adds item in cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieves item by key.
        """
        return self.cache_data.get(key, None)
